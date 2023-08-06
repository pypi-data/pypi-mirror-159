import datetime
from inspect import isclass
from typing import Any, Callable, Dict, Type



# Stock serializable objects. Any user defined object that implements
# the __str__ method can also serialized
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


def normalize_path(path: str) -> str:
    """Normalize all URL paths to have leading '/' and single delimited '/'"""
    if not isinstance(path, str):
        return path
    splits = path.split('/')
    normalized = '/' + '/'.join([split for split in splits if split])
    return normalized


def serialize_arbitrary_to_str(value: Any) -> str:
    """Serialize an arbitrary object with a valid serializer to str"""
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


def serialize_user_obj_to_str(obj: Any) -> str:
    """Serialize a user defined object that implements the __str__ method"""
    if isclass(obj):
        raise ValueError(f"Uninitialized type {obj.__name__}")
    try:
        if type(obj).__str__ is not object.__str__:
            return obj.__str__()
    except AttributeError:
        pass
    raise ValueError("Value must have user implemented '__str__' method")


def default_query_param_formatter(key: str, val: Any) -> str:
    """Serialize key-value pair to string"""
    return f"{key}={serialize_arbitrary_to_str(val)}"