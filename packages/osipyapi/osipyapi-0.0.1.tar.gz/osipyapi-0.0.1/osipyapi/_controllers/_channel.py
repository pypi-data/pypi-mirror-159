from uhttp import RestApi

from ._base import channel_api as api



class Channel:

    @api.endpoint('/instances')
    def get_instances():
        """
        https://docs.osisoft.com/bundle/pi-web-api-reference/page/help/controllers/channel/actions/instances.html
        """