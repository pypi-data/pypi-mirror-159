import asyncio
import concurrent.futures
import itertools
import math
import pytz
from datetime import datetime, timedelta
from types import TracebackType
from typing import (
    Dict,
    List,
    Sequence,
    Set,
    Tuple,
    Type
)

import pandas as pd
import polars as pl
from attrs import define, field
from uhttp import URL

from ._api import pi_web_api
from ._client import PiClient
from ._enums import BatchDataType
from ._types import JSONType



INTERPOLATE_DTYPES = ('Float16', 'Float32', 'Float64')
FFILL_DTYPES = ('Int16', 'Int32', 'Digital', 'String', 'Blob')


def split_interpolated_range(
    start_time: datetime,
    end_time: datetime,
    interval: timedelta,
    num_streams: int,
    max_items_per_request: int
) -> Tuple[List[datetime], List[datetime]]:
    request_timedelta: timedelta = end_time - start_time
    request_time_range = request_timedelta.total_seconds()
    # interpolated data is determinite, we know how many items to expect based
    # on the time range and the interval so we can generate an optimized
    # date range
    items_requested = math.ceil(request_time_range / interval.total_seconds() * num_streams)
    if items_requested < max_items_per_request:
        return [start_time], [end_time]
    s = start_time
    e = end_time
    dt = math.floor(interval.total_seconds() * max_items_per_request / num_streams)
    return split_range(s, e, dt)


def split_recorded_range(
    start_time: datetime,
    end_time: datetime,
    num_streams: int,
    max_items_per_request: int
) -> Tuple[List[datetime], List[datetime]]:
    request_timedelta: timedelta = end_time - start_time
    request_time_range = request_timedelta.total_seconds()
    # assumed 1 item per second
    # we dont know how many data points to expect for any given request but
    # if we ask for too much PI wont raise an error it just wont return everything
    # quietly so we hedge our bets by saying that no point will maintain an
    # average frequency of 1 item per second (which is probably a safe bet)
    items_requested = math.ceil(request_time_range * num_streams)
    if items_requested < max_items_per_request:
        return [start_time], [end_time]
    s = start_time
    e = end_time
    dt = math.floor(max_items_per_request / num_streams)
    return split_range(s, e, dt)


def split_range(
    s: datetime,
    e: datetime,
    dt: int
) -> Tuple[List[datetime], List[datetime]]:
    start_times = []
    end_times = []
    while s < e:
        start_times.append(s)
        # generates next end time at whatever time produces max_rows
        next_timestamp = s + timedelta(seconds=dt)
        if next_timestamp >= e:
            s = e
        else:
            s = next_timestamp
        end_times.append(s)
    return start_times, end_times


def convert_to_frame(
    web_ids: Set[str],
    url_map: Dict[URL, str],
    contents: Dict[URL, List[JSONType]]
) -> pl.DataFrame:
    assert len(url_map) == len(contents)
    web_ids = list(web_ids)
    remapped = {web_id: [] for web_id in web_ids}
    for url, web_id in url_map.items():
        if contents[url]:
            remapped[web_id].append(contents[url]['Items'])
        else:
            remapped[web_id].append(list())
    # lazily stack all responses that share a common web_id
    contents = [
        itertools.chain.from_iterable(remapped[web_id]) for web_id in web_ids
    ]
    raw = {web_id: {'Timestamp': [], 'Value': []} for web_id in web_ids}
    dummy_timestamp = None
    for web_id, content in zip(web_ids, contents):
        for item in content:
            timestamp = item['Timestamp']
            good = item['Good']
            errors = item.get('Errors')
            if errors or not good:
                value = None
            else:
                value = item['Value']
                if isinstance(value, dict):
                    value = value['Name']
            raw[web_id]['Timestamp'].append(timestamp)
            raw[web_id]['Value'].append(value)
            if dummy_timestamp is None:
                dummy_timestamp = timestamp
    frames = []
    for web_id, data in raw.items():
        # convert data item values to DataFrame
        if not data['Value']:
            # this will get
            data['Timestamp'].append(dummy_timestamp)
            data['Value'].append(None)
        frame = pl.DataFrame(
            data=data,
            columns=['Timestamp', web_id]
        )
        if not frame.is_empty():
            frames.append(frame.lazy())
    seed_frame = pl.DataFrame(
        columns=['Timestamp']
    ).select(
        pl.col('Timestamp').cast(str)
    ).lazy()
    for frame in frames:
        seed_frame = seed_frame.join(frame, on='Timestamp', how='outer').unique()
    return seed_frame.sort(
        by='Timestamp'
    ).with_column(
        pl.col(
            'Timestamp'
        ).str.strptime(
            pl.Datetime,
            '%Y-%m-%dT%H:%M:%S%.fZ'
        )
    ).collect()


def get_recorded_endpopint_frame(
    web_ids: Set[str],
    url_map: Dict[URL, str],
    contents: Dict[URL, Dict[str, JSONType]],
    time: datetime,
    timezone: pytz.BaseTzInfo
) -> pl.DataFrame:
    t_utc = timezone.localize(
        time
    ).astimezone(
        pytz.UTC
    ).replace(tzinfo=None).isoformat() + 'Z'
    data = {'Timestamp': [t_utc]}
    data.update({web_id: [] for web_id in web_ids})
    for url, web_id in url_map.items():
        content = contents[url]
        if content:
            good = content['Good']
            if not good:
                value = None
            else:
                value = content['Value']
                if isinstance(value, dict):
                    value = value['Name']
            data[web_id].append(value)
        else:
            data[web_id].append(None)
    return pl.DataFrame(data).with_column(
        pl.col(
            'Timestamp'
        ).str.strptime(
            pl.Datetime,
            '%Y-%m-%dT%H:%M:%S%.fZ'
        ).dt.with_time_zone(timezone.zone)
    )


def interpolate_recorded_frame(
    dtype_map: Dict[str, str],
    frame: pd.DataFrame
) -> pd.DataFrame:
    ts_index = frame.set_index('Timestamp')
    columns = ts_index.columns
    for web_id in columns:
        dtype = dtype_map.get(web_id)
        if dtype is not None:
            if dtype in INTERPOLATE_DTYPES:
                ts_index.loc[:, web_id].interpolate(method='time', inplace=True)
            elif dtype in FFILL_DTYPES:
                ts_index.loc[:, web_id].fillna(method='ffill', inplace=True)
    return ts_index.reset_index()


@define
class BatchDataClient:
    """
    Asynchronous batch data processor for interpolated or recorded data

    The batch data client takes an arbitrary number of WebId's associated to
    PI points and returns an M x N dataframe the number of columns is equivalent
    to the number of unique WebId's passed

    Parameters
    - client (PiClient): the http client used to complete requests
    """
    client: PiClient
    _executor: concurrent.futures.Executor = field(
        factory=lambda: concurrent.futures.ProcessPoolExecutor(max_workers=4),
        init=False
    )

    def get(
        self,
        web_ids: Sequence[str],
        data_type: str,
        start_time: datetime,
        end_time: datetime = None,
        timezone: str = 'US/Eastern',
        max_items: int = 150000,
        interval: timedelta = None,
        interpolate_recorded: bool = False
    ) -> asyncio.Task:
        """
        Submit a batch data request job. This method returns a task which
        represents the eventual completion of the batch data job

        Parameters
        - web_ids (Sequence[str]): the web_ids to collect data for
        - data_type (str): 'interpolated' or 'recorded'
        - start_time (datetime): the start time of the batch
        - end_time (datetime): the end time of the batch
        - timezone (str): the local timezone to convert timestamps too. PI
        returns all requests in UTC time offset relative to the timezone of the
        local server. Specifying a timezone ensures the timestamps are offset
        appropriately back to local time
        - max_items (int): the maximum number of data points that PI can return
        in a single request. the default for PI Web API servers is 150,000
        - interval (timedelta): for 'interpolated' data only, specify the interval
        to return interpolated data on
        - interpolate_recorded (bool): for 'recorded' data only, use the data
        types of the points from PI to interpolate the missing data in the
        recorded frame

        Returns
        - pd.DataFrame

        Notes
        - 'interpolated' data will always return a value for each WebId at the
        interval specified. The size of these dataframes is deterministic and
        are almost always smaller than their 'recorded' counterparts
        - 'recorded' data is lossless, every recorded value for a PI point will
        be returned and joined on a common timestamp index. These frames can
        get VERY LARGE very quickly. The size tends to grow exponentially with
        the number of points that are added because the timestamps for two
        different points in the same date range hardly ever have collisions
        """
        web_ids = set(web_ids)
        data_type = BatchDataType.get_dtype(data_type)
        timezone = pytz.timezone(timezone)
        selected_fields = (
            'Items.Timestamp',
            'Items.Good',
            'Items.Value'
        )
        end_time = end_time or datetime.now()
        if data_type is BatchDataType.INTERPOLATED:
            return self.client.loop.create_task(
                self.handle_interpolated_streams(
                    web_ids,
                    start_time,
                    end_time,
                    timezone,
                    max_items,
                    interval,
                    selected_fields
                )
            )
        elif data_type is BatchDataType.RECORDED:
            return self.client.loop.create_task(
                self.handle_recorded_streams(
                    web_ids,
                    start_time,
                    end_time,
                    timezone,
                    max_items,
                    interpolate_recorded,
                    selected_fields
                )
            )

    async def close(self) -> None:
        self._executor.shutdown()
        await self.client.close()

    async def handle_interpolated_streams(
        self,
        web_ids: Set[str],
        start_time: datetime,
        end_time: datetime,
        timezone: str,
        max_items: int,
        interval: timedelta,
        selected_fields: List[str]
    ) -> pd.DataFrame:
        interval = interval or timedelta(seconds=3600)
        start_times, end_times = split_interpolated_range(
            start_time,
            end_time,
            interval,
            1,
            max_items
        )
        url_map = {}
        urls = []
        for web_id in web_ids:
            for start_time, end_time in zip(start_times, end_times):
                url = pi_web_api.stream.get_interpolated(
                    web_id,
                    start_time=start_time,
                    end_time=end_time,
                    interval=interval,
                    selected_fields=selected_fields
                )
                url_map[url.target] = web_id
                urls.append(url)
        contents = await self.handle_requests(urls)
        processed_frame = await self.client.loop.run_in_executor(
            self._executor,
            convert_to_frame,
            web_ids,
            url_map,
            contents
        )
        frame = processed_frame.with_column(
            pl.col('Timestamp').dt.with_time_zone(timezone.zone)
        ).to_pandas()
        frame.loc[:, 'Timestamp'] = frame.loc[:, 'Timestamp'].dt.tz_localize(None)
        return frame

    async def handle_recorded_streams(
        self,
        web_ids: Set[str],
        start_time: datetime,
        end_time: datetime,
        timezone: str,
        max_items: int,
        interpolate_recorded: bool,
        selected_fields: List[str]
    ) -> pd.DataFrame:
        web_ids = list(web_ids)
        endpoint_frames: Tuple[pl.DataFrame, pl.DataFrame] = await self.handle_recorded_endpoints(
            web_ids,
            start_time,
            end_time,
            timezone
        )
        start_times, end_times = split_recorded_range(
            start_time,
            end_time,
            1,
            max_items
        )
        url_map = {}
        urls = []
        for web_id in web_ids:
            for start_time, end_time in zip(start_times, end_times):
                url = pi_web_api.stream.get_recorded(
                    web_id,
                    start_time=start_time,
                    end_time=end_time,
                    max_count=max_items,
                    selected_fields=selected_fields
                )
                url_map[url.target] = web_id
                urls.append(url)
        contents = await self.handle_requests(urls)
        processed_frame = await self.client.loop.run_in_executor(
            self._executor,
            convert_to_frame,
            web_ids,
            url_map,
            contents
        )
        main_frame = processed_frame.with_column(
            pl.col('Timestamp').dt.with_time_zone(timezone.zone)
        )
        frame = endpoint_frames[0].vstack(
            main_frame
        ).vstack(
            endpoint_frames[1]
        ).to_pandas()
        frame.loc[:, 'Timestamp'] = frame.loc[:, 'Timestamp'].dt.tz_localize(None)
        if interpolate_recorded:
            dtype_map = await self.get_point_dtypes(web_ids)
            return interpolate_recorded_frame(dtype_map, frame)
        return frame

    async def handle_recorded_endpoints(
        self,
        web_ids: Set[str],
        start_time: datetime,
        end_time: datetime,
        timezone: pytz.BaseTzInfo
    ) -> Tuple[pl.DataFrame, pl.DataFrame]:
        frames = []
        for time in (start_time, end_time):
            url_map = {}
            urls = []
            for web_id in web_ids:
                url = pi_web_api.stream.get_recorded_at_time(
                    web_id,
                    time,
                    selected_fields=[
                        'Timestamp',
                        'Value',
                        'Good'
                    ]
                )
                url_map[url.target] = web_id
                urls.append(url)
            contents = await self.handle_requests(urls)
            frames.append(
                get_recorded_endpopint_frame(
                    web_ids,
                    url_map,
                    contents,
                    time,
                    timezone
                )
            )
        return frames[0], frames[1]

    async def get_point_dtypes(self, web_ids: Set[str]) -> Dict[str, str]:
        urls = [
            pi_web_api.point.get(
                web_id,
                selected_fields=['WebId', 'PointType']
            ) for web_id in web_ids
        ]
        dispatch = [self.client.get(url) for url in urls]
        responses = await asyncio.gather(*dispatch)
        dtype_map = {}
        for response in responses:
            content = response.content
            if response.status_code == 200 and isinstance(content, dict):
                dtype_map[content['WebId']] = content['PointType']
        return dtype_map

    async def handle_requests(self, urls: List[URL]) -> Dict[URL, List[JSONType]]:
        dispatch = [self.client.get(url) for url in urls]
        responses = await asyncio.gather(*dispatch)
        contents = {}
        for url, response in zip(urls, responses):
            target = url.target
            content = response.content
            if response.status_code == 200 and isinstance(content, dict):
                contents[target] = content
            else:
                contents[target] = None
        return contents

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type: Type[BaseException] = None,
        exc_value: BaseException = None,
        traceback: TracebackType = None,
    ) -> None:
        await self.close()