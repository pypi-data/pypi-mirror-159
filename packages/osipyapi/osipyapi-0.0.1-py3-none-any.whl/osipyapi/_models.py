import orjson
from attrs import define
from uhttp import H11Response, Headers

from ._types import JSONType



@define
class PiResponse:
    response: H11Response
    content: JSONType

    @property
    def headers(self) -> Headers:
        return self.response.headers

    @property
    def status_code(self) -> int:
        return self.response.status_code

    def raise_for_status(self) -> None:
        self.response.raise_for_status()

    def raise_for_err(self) -> None:
        if isinstance(self.content, orjson.JSONDecodeError):
            raise self.content
        if self.content is None:
            raise ValueError("No data returned")