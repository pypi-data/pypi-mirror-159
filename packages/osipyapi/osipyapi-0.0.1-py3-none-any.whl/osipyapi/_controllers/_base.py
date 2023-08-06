from uhttp import RestApi

from .._util import DefaultQueryParam, MultiInstQueryParam, SemiColQueryParam



assetdatabase_api = RestApi(
    '/piwebapi/assetdatabases',
    always_cast=dict(selected_fields=SemiColQueryParam),
    default_query_type=DefaultQueryParam
)
assetserver_api = RestApi(
    '/piwebapi/assetservers',
    always_cast=dict(selected_fields=SemiColQueryParam),
    default_query_type=DefaultQueryParam
)
attribute_api = RestApi(
    '/piwebapi/attributes',
    always_cast=dict(selected_fields=SemiColQueryParam),
    default_query_type=DefaultQueryParam
)
channel_api = RestApi('/piwebapi/channels')
dataserver_api = RestApi(
    '/piwebapi/dataservers',
    always_cast=dict(selected_fields=SemiColQueryParam),
    default_query_type=DefaultQueryParam
)
element_api = RestApi(
    '/piwebapi/elements',
    always_cast=dict(
        selected_fields=SemiColQueryParam,
        associations=SemiColQueryParam
    ),
    default_query_type=DefaultQueryParam
)
point_api = RestApi(
    '/piwebapi/points',
    always_cast=dict(selected_fields=SemiColQueryParam),
    default_query_type=DefaultQueryParam
)
stream_api = RestApi(
    '/piwebapi/streams',
    always_cast=dict(selected_fields=SemiColQueryParam),
    default_query_type=DefaultQueryParam
)
streamset_api = RestApi(
    '/piwebapi/streamsets',
    always_cast=dict(
        web_id=MultiInstQueryParam,
        selected_fields=SemiColQueryParam
    ),
    default_query_type=DefaultQueryParam
)