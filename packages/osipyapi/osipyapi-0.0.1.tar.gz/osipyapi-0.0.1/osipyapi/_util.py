import datetime
import re
from inspect import isclass
from typing import (
    Any,
    Callable,
    Dict,
    Type
)

from uhttp import QueryParam



# valid types to serialize to str
SERIALIZERS_BY_TYPE: Dict[Type[Any], Callable[[Any], str]] = {
    bytes: lambda o: o.decode(),
    bool: str,
    datetime.date: lambda dt: dt.isoformat(),
    datetime.datetime: lambda dt: dt.isoformat(sep='T'),
    datetime.time: lambda dt: dt.isoformat(),
    datetime.timedelta: lambda td: f"{td.total_seconds()} seconds",
    float: str,
    int: str
}


def serialize_user_obj_to_str(obj: Any) -> str:
    if isclass(obj):
        raise ValueError(f"Uninstantiated type {obj.__name__}")
    try:
        if type(obj).__str__ is not object.__str__:
            return obj.__str__()
    except AttributeError:
        pass
    raise ValueError("Value must have user implemented '__str__' method")


def serialize_arbitrary_to_str(value: Any) -> str:
    if isinstance(value, str):
        return value
    for base in value.__class__.__mro__[:-1]:
        try:
            serializer = SERIALIZERS_BY_TYPE[base]
        except KeyError:
            continue
        return serializer(value)
    try:
        return serialize_user_obj_to_str(value)
    except ValueError:
        pass
    raise TypeError(
        f"Unable to serialize obj of type {type(value)} to str"
    )


def camel_case_to_snake_case(key: str) -> str:
    split = re.findall(r"[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))", key)
    if split:
        return "_".join([val.lower() for val in split])
    return key.lower()


def snake_case_to_lower_camel_case(key: str) -> str:
    split = key.split("_")
    if len(split) > 1:
        key = split[0] + "".join(
            [val.title() for val in split[1:]]
        )
    return key


def snake_case_to_camel_case(key: str) -> None: 
    split = key.split("_")
    if len(split) > 1:
        key = "".join(
            [val.title() for val in split]
        )
        return key
    else:
        return key.title()


class DefaultQueryParam(QueryParam):
    def to_str(self):
        return (
            f"{snake_case_to_lower_camel_case(self.key)}="
            f"{serialize_arbitrary_to_str(self.val)}"
        )


class MultiInstQueryParam(QueryParam):
    def to_str(self):
        ret = ""
        for i, val in enumerate(self.val):
            if i > 0:
                ret += "&"
            ret += f"{snake_case_to_lower_camel_case(self.key)}={val}"
        return ret


class SemiColQueryParam(QueryParam):
    def to_str(self):
        return (
            f"{snake_case_to_lower_camel_case(self.key)}={';'.join(self.val)}"
        )
    