from typing import List



class PiClientError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class SubscriptionError(PiClientError):
    def __init__(self, not_subscribed: List[str]) -> None:
        self.not_subscribed = not_subscribed

    def __str__(self) -> str:
        return (
            "Max streams reached. Could not subscribe to the following WebId's\n"
            "{not_subscribed}".format(not_subscibed='\n'.join(self.not_subscribed))
        )


class HttpClientError(PiClientError):
    def __init__(self, reason: Exception) -> None:
        self.reason = reason

    def __str__(self) -> str:
        return f"Caused by - {repr(self.reason)}"