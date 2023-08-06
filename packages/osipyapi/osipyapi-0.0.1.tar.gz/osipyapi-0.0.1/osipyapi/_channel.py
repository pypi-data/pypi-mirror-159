import asyncio
import functools
import logging
from ssl import SSLContext
from types import TracebackType
from typing import (
    Callable,
    Coroutine,
    Dict,
    List,
    Sequence,
    Set,
    Tuple,
    Type,
    Union
)

import orjson
from attrs import define, field
from uhttp import Auth, Headers, Origin, Request, W11Protocol
from uhttp_negotiate import NegotiateAuth

from ._api import pi_web_api
from ._enums import ChannelState
from ._exceptions import SubscriptionError



@define
class PiChannel:
    queue: asyncio.Queue
    failed_callback: Callable[[Exception], None]
    scheme: str
    host: str
    port: int = field(default=None)
    auth: Auth = field(factory=NegotiateAuth)
    headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = field(
        factory=Headers.default_headers, converter=Headers
    )
    ssl: SSLContext = field(default=None)
    close_handshake_timeout: Union[int, float] = field(default=5)
    ping_interval: Union[int, float] = field(default=30)
    ping_timeout: Union[int, float] = field(default=30)
    max_reconnect_attempts: int = field(default=30)
    max_backoff: Union[int, float] = field(default=60)
    logger: logging.Logger = field(
        factory=functools.partial(logging.getLogger, __name__)
    )
    loop: asyncio.AbstractEventLoop = field(factory=asyncio.get_event_loop)
    _origin: Origin = field(default=None, init=False)
    _connection: W11Protocol = field(default=None, init=False)
    _connection_lock: asyncio.Lock = field(factory=asyncio.Lock, init=False)
    _close_task: asyncio.Task = field(default=None, init=False)
    _close_waiter: asyncio.Future = field(default=None, init=False)
    _ready: asyncio.Event = field(factory=asyncio.Event, init=False)
    _state: ChannelState = field(default=ChannelState.CLOSED, init=False)
    _subscriptions: List[str] = field(factory=list, init=False)

    def __attrs_post_init__(self):
        origin = Origin(self.scheme, self.host, self.port)
        self._connection = W11Protocol(
            origin,
            self.ssl,
            logger=self.logger,
            loop=self.loop,
            max_reconnect_attempts=self.max_reconnect_attempts,
            max_backoff=self.max_backoff,
            close_handshake_timeout=self.close_handshake_timeout,
            ping_interval=self.ping_interval,
            ping_timeout=self.ping_timeout
        )
        self._origin = origin

    @property
    def state(self) -> ChannelState:
        return self._state

    @property
    def subscriptions(self) -> List[str]:
        return self._subscriptions

    async def start(self, web_ids: Sequence[str]) -> None:
        async with self._connection_lock:
            if self._state is not ChannelState.CLOSED:
                raise RuntimeError(
                    f"Cannot start channel in state {self._state.name}"
                )
            self._state = ChannelState.OPENING
            url = pi_web_api.stream_set.get_channel_adhoc(web_ids)
            url = url.copy_with_origin(self._origin)
            request = Request(
                'GET',
                url,
                self.headers
            )
            await self._connection.aconnect()
            await self._connection.ahandshake(request, self.auth)
            task = self.loop.create_task(self.recieve_task())
            self._close_task = self.loop.create_task(self.closing_task(task))
            await self._ready.wait()
            self._state = ChannelState.OPEN
            self._subscriptions.extend(web_ids)

    async def stop(self) -> None:
        async with self._connection_lock:
            if self._state is ChannelState.CLOSED:
                return
            close_task = self._close_task
            self._close_task = None
            assert close_task is not None and not close_task.done()
            if self._state is ChannelState.CLOSING:
                return await close_task
            close_waiter = self._close_waiter
            self._close_waiter = None
            assert close_waiter is not None and not close_waiter.done()
            close_waiter.set_result(None)
            await asyncio.shield(close_task)

    async def recieve_task(self) -> None:
        assert self._connection._ws_state.name == 'OPEN'
        async for raw_message in self._connection:
            try:
                message = orjson.loads(raw_message)
            except orjson.JSONDecodeError:
                pass
            else:
                await self.queue.put(message)

    async def closing_task(self, receive_task: asyncio.Task) -> None:
        waiter = self.loop.create_future()
        self._close_waiter = waiter
        self._ready.set()
        try:
            await asyncio.wait(
                [receive_task, waiter], return_when=asyncio.FIRST_COMPLETED
            )
        except asyncio.CancelledError:
            receive_task.cancel()
            waiter.cancel()
            self._close_waiter = None
            self._subscriptions.clear()
            self._state = ChannelState.CLOSED
            # Websocket protocol's interrupt helper will ensure close frame
            # is sent and transport is closed
            raise
        if waiter.done():
            # stop called
            receive_task.cancel()
            await self.close_channel()
        else:
            # receive task finished, websocket failed (this also means the
            # websocket was unable to reconnect)
            waiter.cancel()
            self._close_waiter = None
            exc = None
            try:
                await receive_task
            except BaseException as err:
                exc = err
            await self.close_channel()
            assert exc is not None
            self.loop.call_soon(self.failed_callback, exc)

    async def close_channel(self) -> None:
        self._state = ChannelState.CLOSING
        try:
            await self._connection.aclose()
        finally:
            self._subscriptions.clear()
            self._state = ChannelState.CLOSED
            
        
@define
class ChannelPool:
    scheme: str
    host: str
    port: int = field(default=None)
    failed_callback: Callable[[BaseException], None] = field(default=None)
    auth: Auth = field(factory=NegotiateAuth)
    max_connections: int = field(default=50)
    max_streams_per_connection: int = field(default=50)
    max_buffered_messages: int = field(default=2000)
    headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = field(
        factory=Headers.default_headers, converter=Headers
    )
    ssl: SSLContext = field(default=None)
    close_handshake_timeout: Union[int, float] = field(default=5)
    ping_interval: Union[int, float] = field(default=30)
    ping_timeout: Union[int, float] = field(default=30)
    max_reconnect_attempts: int = field(default=30)
    max_backoff: Union[int, float] = field(default=60)
    logger: logging.Logger = field(
        factory=functools.partial(logging.getLogger, __name__)
    )
    loop: asyncio.AbstractEventLoop = field(factory=asyncio.get_event_loop)
    _origin: Origin = field(default=None, init=False)
    _queue: asyncio.Queue = field(default=None, init=False)
    _pool: List[PiChannel] = field(factory=list, init=False)
    _pool_lock: asyncio.Lock = field(factory=asyncio.Lock, init=False)
    _subscriptions: Set[str] = field(factory=set, init=False)

    def __attrs_post_init__(self) -> None:
        self._origin = Origin(self.scheme, self.host, self.port)
        self._queue = asyncio.Queue(self.max_buffered_messages)

    async def subscribe(self, web_ids: Sequence[str]) -> None:
        async with self._pool_lock:
            self.sync_subscriptions()
            to_start = []
            to_stop = []
            to_add = list(set(web_ids) - self._subscriptions)
            if to_add:
                # check current channels to see if any of them can take on
                # new subscriptions
                for channel in self._pool:
                    channel_subs = list(channel.subscriptions)
                    if len(channel_subs) <= self.max_streams_per_connection:
                        # get number of available subscriptions channel can
                        # take on
                        available = self.max_streams_per_connection - len(channel_subs)
                        if len(to_add) <= available:
                            # channel can take on all the new subscriptions
                            channel_subs.extend(to_add)
                            to_stop.append(channel.stop())
                            to_start.append(channel.start(channel_subs))
                            return await self.start_stop_channels(
                                to_start,
                                to_stop
                            )
                        else:
                            # we cant subscribe to all web_ids on that channel.
                            # subscribe to what we can and move onto the next
                            # channel
                            channel_subs.extend(to_add[:available])
                            del to_add[:available]
                            to_stop.append(channel.stop())
                            to_start.append(channel.start(channel_subs))
                if to_add:
                    # we've gone through all our open channels and determined
                    # we dont have enough existing channels to subscribe to
                    # everything
                    while True:
                        if len(self._pool) >= self.max_connections:
                            # we've reached the connection cap, we cant subscribe
                            # to anymore
                            await self.start_stop_channels(
                                to_start,
                                to_stop
                            )
                            raise SubscriptionError(to_add)
                        channel = PiChannel(
                            self._queue,
                            self.channel_failed,
                            self.scheme,
                            self.host,
                            self.port,
                            self.auth,
                            self.headers,
                            self.ssl,
                            self.close_handshake_timeout,
                            self.ping_interval,
                            self.ping_timeout,
                            self.max_reconnect_attempts,
                            self.max_backoff,
                            self.logger,
                            self.loop
                        )
                        self._pool.insert(0, channel)
                        channel_subs = list()
                        available = self.max_streams_per_connection
                        if len(to_add) <= available:
                            channel_subs.extend(to_add)
                            to_start.append(channel.start(channel_subs))
                            return await self.start_stop_channels(
                                to_start,
                                to_stop
                            )
                        else:
                            channel_subs.extend(to_add[:available])
                            del to_add[:available]
                            to_start.append(channel.start(channel_subs))

    async def unsubscribe(self, web_ids: Sequence[str]) -> None:
        async with self._pool_lock:
            self.sync_subscriptions()
            to_start = []
            to_stop = []
            dne = set(web_ids) - self._subscriptions
            to_remove = set(web_ids) - dne
            for channel in self._pool:
                to_keep = set(channel.subscriptions) - set(to_remove)
                if len(to_keep) != len(channel.subscriptions):
                    # we are removing one, many or all subscriptions from this
                    # channel
                    to_stop.append(channel.stop())
                    # this channel will still support some subscriptions
                    if to_keep:
                        to_start.append(channel.start(to_keep))
            await self.start_stop_channels(to_start, to_stop)

    async def close(self) -> None:
        async with self._pool_lock:
            await asyncio.gather(*[channel.stop() for channel in self._pool])
            self._pool = list()

    async def start_stop_channels(
        self,
        to_start: List[Coroutine[None, Sequence[str], None]],
        to_stop: List[Coroutine[None, None, None]]
    ) -> None:
        if to_stop:
            await asyncio.gather(*to_stop)
        if to_start:
            await asyncio.gather(*to_start)
        self.sync_subscriptions()

    async def __aiter__(self):
        while True:
            message = await self._queue.get()
            yield message

    def channel_failed(self, exc: BaseException) -> None:
        self.sync_subscriptions()
        self.logger.warning(f"Channel failed: {repr(exc)}")
        if self.failed_callback is not None:
            self.loop.call_soon(self.failed_callback, exc)

    def sync_subscriptions(self) -> None:
        for idx, channel in reversed(list(enumerate(self._pool))):
            if channel.state is ChannelState.CLOSED:
                self._pool.pop(idx)
        for channel in self._pool:
            self._subscriptions.update(channel.subscriptions)

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> None:
        await self.close()
        