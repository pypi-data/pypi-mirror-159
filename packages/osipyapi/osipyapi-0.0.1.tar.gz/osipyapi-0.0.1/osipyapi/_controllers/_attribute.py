from typing import Sequence

from ._base import attribute_api as api
from .._util import MultiInstQueryParam, SemiColQueryParam



class Attribute:
    """
    https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/attribute.html
    """

    @api.endpoint(
        '/{web_id}',
        cast=dict(associations=SemiColQueryParam)
    )
    @staticmethod
    def get(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
        associations: Sequence[str] = None
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/attribute/actions/get.html
        """

    @api.endpoint(cast=dict(associations=SemiColQueryParam))
    @staticmethod
    def get_by_path(
        path: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
        associations: Sequence[str] = None
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/attribute/actions/getbypath.html
        """

    @api.endpoint(
        '/mulitple',
        cast=dict(
            web_id=MultiInstQueryParam,
            path=MultiInstQueryParam,
            associations=SemiColQueryParam
        )
    )
    @staticmethod
    def get_multiple(
        web_id: Sequence[str] = None,
        path: Sequence[str] = None,
        include_mode: str = None,
        as_parallel: bool = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
        associations: Sequence[str] = None
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/attribute/actions/getmultiple.html
        """
        if web_id is None and path is None:
            raise ValueError("Must specify one of either 'web_id' or 'path'")

    @api.endpoint('/{web_id}/value')
    @staticmethod
    def get_value(
        web_id: str,
        selected_fields: Sequence[str] = None
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/attribute/actions/getvalue.html
        """

    @api.endpoint(
        '/{web_id}/attributes',
        cast=dict(
            associations=SemiColQueryParam,
            trait=MultiInstQueryParam,
        )
    )
    @staticmethod
    def get_attributes(
        web_id: str,
        name_filter: str = None,
        category_name: str = None,
        template_name: str = None,
        value_type: str = None,
        search_full_hierarchy: bool = None,
        sort_field: str = None,
        sort_order: str = None,
        start_index: int = None,
        show_excluded: bool = None,
        show_hidden: bool = None,
        max_count: int = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
        associations: Sequence[str] = None,
        trait: Sequence[str] = None,
        trait_category: str = None
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/element/actions/getattributes.html
        """