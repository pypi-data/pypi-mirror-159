import asyncio
import functools
import logging
from ssl import SSLContext
from types import TracebackType
from typing import AsyncIterable, Dict, Tuple, Type, Union

import orjson
from attrs import define, field
from uhttp import Auth, H11Pool, Headers, Origin, Request, URL
from uhttp_negotiate import NegotiateAuth

from ._exceptions import HttpClientError
from ._models import PiResponse
from ._types import JSONType



@define
class PiClient:
    scheme: str
    host: str
    port: int = field(default=None)
    auth: Auth = field(factory=NegotiateAuth)
    headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = field(
        factory=Headers.default_headers, converter=Headers
    )
    ssl: SSLContext = field(default=None)
    max_connections: int = field(default=50)
    acquire_connection_timeout: Union[int, float, None] = field(default=30)
    logger: logging.Logger = field(
        factory=functools.partial(logging.getLogger, __name__)
    )
    loop: asyncio.AbstractEventLoop = field(factory=asyncio.get_event_loop)
    _origin: Origin = field(default=None, init=False)
    _pool: H11Pool = field(default=None, init=False)

    def __attrs_post_init__(self) -> None:
        origin = Origin(self.scheme, self.host, self.port)
        self._pool = H11Pool(
            origin,
            auth=self.auth,
            max_connections=self.max_connections,
            ssl=self.ssl,
            acquire_connection_timeout=self.acquire_connection_timeout
        )
        self._origin = origin

    async def close(self) -> None:
        await self._pool.aclose()

    async def request(
        self,
        method: str,
        url: URL,
        auth: Auth = None,
        headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = None,
        content: Union[AsyncIterable[bytes], bytes, bytearray, str, JSONType, None] = None,
        read_timeout: Union[int, float, None] = 10,
        write_timeout: Union[int, float, None] = 10
    ):
        url = url.copy_with_origin(self._origin)
        auth = auth or self.auth
        headers = Headers(headers) if headers is not None else self.headers
        timeouts = dict(read=read_timeout, write=write_timeout)
        request = Request(
            method,
            url,
            headers,
            content,
            timeouts
        )
        if request.method.name not in ('POST', 'PATCH', 'PUT') and request.content is not None:
            raise ValueError(f"Cannot send content in a {request.method.name} request")
        try:
            response = await self._pool.arequest(request, auth)
            content = await response.aread()
        except BaseException as err:
            raise HttpClientError(err)
        if content:
            try:
                content = orjson.loads(content)
            except orjson.JSONDecodeError as err:
                content = err
        else:
            content = None
        return PiResponse(
            response.response,
            content,
        )

    async def get(
        self,
        url: URL,
        auth: Auth = None,
        headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = None,
        read_timeout: Union[int, float, None] = 10,
        write_timeout: Union[int, float, None] = 10
    ) -> PiResponse:
        return await self.request(
            'GET',
            url,
            auth,
            headers,
            None,
            read_timeout,
            write_timeout
        )

    async def post(
        self,
        url: URL,
        auth: Auth = None,
        headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = None,
        content: Union[AsyncIterable[bytes], bytes, bytearray, str, JSONType, None] = None,
        read_timeout: Union[int, float, None] = 10,
        write_timeout: Union[int, float, None] = 10
    ) -> PiResponse:
        return await self.request(
            'POST',
            url,
            auth,
            headers,
            content,
            read_timeout,
            write_timeout
        )

    async def put(
        self,
        url: URL,
        auth: Auth = None,
        headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = None,
        content: Union[AsyncIterable[bytes], bytes, bytearray, str, JSONType, None] = None,
        read_timeout: Union[int, float, None] = 10,
        write_timeout: Union[int, float, None] = 10
    ) -> PiResponse:
        return await self.request(
            'PUT',
            url,
            auth,
            headers,
            content,
            read_timeout,
            write_timeout
        )

    async def patch(
        self,
        url: URL,
        auth: Auth = None,
        headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = None,
        content: Union[AsyncIterable[bytes], bytes, bytearray, str, JSONType, None] = None,
        read_timeout: Union[int, float, None] = 10,
        write_timeout: Union[int, float, None] = 10
    ) -> PiResponse:
        return await self.request(
            'PATCH',
            url,
            auth,
            headers,
            content,
            read_timeout,
            write_timeout
        )

    async def delete(
        self,
        url: URL,
        auth: Auth = None,
        headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = None,
        read_timeout: Union[int, float, None] = 10,
        write_timeout: Union[int, float, None] = 10
    ) -> PiResponse:
        return await self.request(
            'DELETE',
            url,
            auth,
            headers,
            None,
            read_timeout,
            write_timeout
        )

    async def option(
        self,
        url: URL,
        auth: Auth = None,
        headers: Union[Dict[str, str], Tuple[str, str], Tuple[bytes, bytes]] = None,
        read_timeout: Union[int, float, None] = 10,
        write_timeout: Union[int, float, None] = 10
    ) -> PiResponse:
        return await self.request(
            'OPTION',
            url,
            auth,
            headers,
            read_timeout,
            write_timeout
        )

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> None:
        await self.close()