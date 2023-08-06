from typing import Sequence

from ._base import point_api as api
from .._util import MultiInstQueryParam



class Point:
    """
    https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/point.html
    """

    @api.endpoint('/{web_id}')
    @staticmethod
    def get(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/point/actions/get.html
        """

    @api.endpoint()
    @staticmethod
    def get_by_path(
        path: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/point/actions/getbypath.html
        """

    @api.endpoint(
        '/mulitple',
        cast=dict(
            web_id=MultiInstQueryParam,
            path=MultiInstQueryParam
        )
    )
    @staticmethod
    def get_multiple(
        web_id: Sequence[str] = None,
        path: Sequence[str] = None,
        include_mode: str = None,
        as_parallel: bool = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/point/actions/getmultiple.html
        """
        if web_id is None and path is None:
            raise ValueError("Must specify one of either 'web_id' or 'path'")