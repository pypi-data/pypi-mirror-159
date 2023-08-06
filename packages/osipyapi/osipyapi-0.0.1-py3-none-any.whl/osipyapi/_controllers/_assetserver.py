from typing import Sequence

from ._base import assetserver_api as api
from .._util import MultiInstQueryParam



class AssetServer:
    """
    https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver.html
    """

    @api.endpoint()
    @staticmethod
    def list(
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/list.html
        """

    @api.endpoint('/{web_id}')
    @staticmethod
    def get(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/get.html
        """

    @api.endpoint()
    @staticmethod
    def get_by_path(
        path: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getbypath.html
        """

    @api.endpoint('/{web_id}/analysisruleplugins')
    @staticmethod
    def get_analysis_rule_plugins(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getanalysisruleplugins.html
        """

    @api.endpoint()
    @staticmethod
    def get_by_name(
        name: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getbyname.html
        """
    
    @api.endpoint('/{web_id}/assetdatabases')
    @staticmethod
    def get_databases(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getdatabases.html
        """
    
    @api.endpoint('/{web_id}/notificationcontacttemplates')
    @staticmethod
    def get_notification_contact_templates(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getnotificationcontacttemplates.html
        """

    @api.endpoint('/{web_id}/notificationplugins')
    @staticmethod
    def get_notification_plugins(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getnotificationplugins.html
        """

    @api.endpoint(
        '/{web_id}/security',
        cast=dict(
            security_identity=MultiInstQueryParam,
            user_identity=MultiInstQueryParam
        )
    )
    @staticmethod
    def get_security(
        web_id: str,
        security_item: Sequence[str] = None,
        user_identity: Sequence[str] = None,
        force_refresh: bool = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getsecurity.html
        """

    @api.endpoint('/{web_id}/securityentries')
    @staticmethod
    def get_security_entries(
        web_id: str,
        security_item: str = None,
        name_filter: str = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getsecurityentries.html
        """
        
    @api.endpoint('/{web_id}/securityentries/{name}')
    @staticmethod
    def get_security_entry_by_name(
        web_id: str,
        name: str,
        security_item: str = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getsecurityentrybyname.html
        """

    @api.endpoint('/{web_id}/securityentries')
    @staticmethod
    def get_security_identities(
        web_id: str,
        query: str = None,
        field: str = None,
        sort_field: str = None,
        sort_order: str = None,
        max_count: int = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getsecurityidentities.html
        """

    @api.endpoint('/{web_id}/securityidentities')
    @staticmethod
    def get_security_identities_for_user(
        web_id: str,
        user_identity: str = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getsecurityidentitiesforuser.html
        """

    @api.endpoint('/{web_id}/securitymappings')
    @staticmethod
    def get_security_mappings(
        web_id: str,
        query: str = None,
        field: str = None,
        sort_field: str = None,
        sort_order: str = None,
        max_count: int = None,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getsecuritymappings.html
        """

    @api.endpoint('/{web_id}/timeruleplugins')
    @staticmethod
    def get_time_rule_plugins(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/gettimeruleplugins.html
        """


    @api.endpoint('/{web_id}/unitclasses')
    @staticmethod
    def get_unit_classes(
        web_id: str,
        selected_fields: Sequence[str] = None,
        web_id_type: str = None,
    ):
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/assetserver/actions/getunitclasses.html
        """