import functools
import inspect
import re
from typing import Any, Callable, Dict, List, OrderedDict

from attrs import define, field
from attrs.validators import instance_of, is_callable
import rfc3986

from ._util import (
    default_query_param_formatter,
    normalize_path,
    serialize_arbitrary_to_str
)



def validate_method_signature(func_params: OrderedDict[str, inspect.Parameter]):
    """Decorated methods cannot have variable postional arguments"""
    for _, (_, param) in enumerate(func_params.items()):
        if param.kind is param.VAR_POSITIONAL:
            raise TypeError(
                "Decorated method cannot have variable positional arguments"
            )


def interpolate_path(
    path: str,
    path_params: List[str],
    func_params: OrderedDict[str, inspect.Parameter],
    args: List[Any],
    kwargs: Dict[str, Any]
) -> str:
    """Inject values from a function into a string with variable path params"""
    matched_params = {}
    # loop through all function parameters in signature and match any
    # param to the param name in the path
    for _, (name, param) in enumerate(func_params.items()):
        if name.lower() == 'self' or name.lower() == 'cls':
            # if wrapping an instance method or classmethod the first argument
            # will be self or cls, we dont want anything to do with that. If
            # someone naively made 'self' a path param, it will raise an error
            # for being unmatched
            args.pop(0)
            continue
        # matched a path param name to func param
        if name in path_params:
            if param.kind is param.VAR_KEYWORD:
                raise ValueError(
                    "Path parameters cannot be variable keyword arguments"
                )
            path_params.remove(name)
            # check the param type to determine where the value should be
            # pulled from
            if param.kind is param.POSITIONAL_ONLY: # must come from args
                val = args.pop(0)
            elif param.kind is param.POSITIONAL_OR_KEYWORD: # can be args or kwargs
                # if we still have args the value must come from args
                if args:
                    val = args.pop(0)
                else:
                    # the value must come from kwargs or a default value is set
                    if name in kwargs:
                        val = kwargs.pop(name)
                    else:
                        val = param.default
            else: # must come from kwargs
                if name in kwargs:
                    val = kwargs.pop(name)
                else:
                    val = param.default
            # the path param must be serializable with default serializers
            matched_params[name] = serialize_arbitrary_to_str(val)
    if path_params:
        raise ValueError(f"Unmatched path params: {', '.join(path_params)}")
    # replace each placeholder '{<name>}' with value
    for name, val in matched_params.items():
        key = '{' + name + '}'
        path = path.replace(key, val)
    return path


def convert_to_kwargs(
    path_params: List[str],
    func_params: OrderedDict[str, inspect.Parameter],
    args: List[Any],
    kwargs: Dict[str, Any]
) -> List[str]:
    """
    Convert any remaining args to kwargs according to the function signature.
    Any remaining args will not be a path param
    """
    for _, (name, param) in enumerate(func_params.items()):
        if name.lower() == 'self' or name.lower() == 'cls':
            continue
        elif name in path_params:
            # path params cannot be query params and the values have already
            # been removed from args and kwargs at this point
            continue
        elif param.kind in (param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD):
            # convert any remaining args to kwargs
            if args:
                kwargs.update({name: args.pop(0)})


def format_query_params(
    formatters: Dict[str, Callable[[str, Any], str]],
    default_formatter: Callable[[str, Any], str],
    kwargs: Dict[str, Any]
) -> List[str]:
    """Format kwargs to str"""
    formatted = []
    for key, val in kwargs.items():
        if val is not None:
            formatter = formatters.get(key, default_formatter)
            formatted.append(formatter(key, val))
    return formatted


@define
class Api:
    """
    Class for converting function args to REST api endpoint urls

    Usage
    ```python
    from rrtarget import Api

    api = Api('mybasepath')
    route = api.router('myroutepath')

    @route.endpoint('myendpoint/{resource}) # define variable path params with {} syntax
    def example_resource(resource: str):
        pass

    url = example_resource('myresource')
    print(url.path)
    >>> /mybasepath/myroutepath/myendpoint/myresource

    @route.endpoint()
    def with_query_params(param: int):
        pass

    url = with_query_params(123)
    print(url.path + '?' + url.query)
    >>> /mybasepath/myroutepath/myendpoint?param=123
    ```

    You can define custom formatters for a query parameter at the root api level
    all the way down to the endpoint. Query param keys which match a key in the
    formatter will use that formatter when converting to 'key=value'. Formatters
    must always return a string with format 'key=value'

    A common error seen with defining endpoints is if you mispell a query param
    in the `formatters` argument, for example...
    ```python
    @route.endpoint(formatters=dict(field=my_formatter))
    def i_screwed_up(fields: List[str]):
        # 'field' is not 'fields'
    ```
    The default formatter will not serialize lists (or any sequence) and will
    raise a TypeError but the error is pretty non-descript. Always check your
    spelling in both your path parameters and custom formatters

    Method signatures cannot contain variable positional arguments (*args).
    They can contain variable keyword arguments (**kwargs). In this case,
    any extra keyword arguments will be formatted by the `default_formatter`
    for the api or router

    Parameters
    - path (str): the base path that all routers and endpoints will inherit
    - formatters (Dict[str, Callable[[str, Any], str]): custom formatters to be
    applied across the whole API. You can specify all formatters for every
    query param in the top level API, if the parameter doesnt exist in method
    it will be ignored
    - default_formatter (Callable[[str, Any], str]): a default formatter to
    use if no custom formatter is defined for given parameter
    """
    path: str = field(
        default='/', converter=normalize_path, validator=instance_of(str)
    )
    formatters: Dict[str, Callable[[str, Any], str]] = field(
        factory=dict, validator=instance_of(dict)
    )
    default_formatter: Callable[[str, Any], str] = field(
        default=default_query_param_formatter, validator=is_callable()
    )

    def router(
        self,
        path: str,
        formatters: Dict[str, Callable[[str, Any], str]] = {},
        default_formatter: Callable[[str, Any], str] = None
    ) -> "Api":
        """
        Return a 'router'

        A 'router' is just another instance of `Api` that merges the path and
        formatters from the parent api. You can override the `default_formatter`
        on a router by router basis by specifying a callable
        """
        path = self.path + normalize_path(path)
        formatters.update(self.formatters)
        default_formatter = default_formatter or self.default_formatter
        return Api(path, formatters, default_formatter)

    def endpoint(
        self,
        path: str = None,
        formatters: Dict[str, Callable[[str, Any], str]] = {},
        default_formatter: Callable[[str, Any], str] = None
    ) -> rfc3986.URIReference:
        """
        Method decorator for defining endpoints

        Functions wrapped by this method should not return anything (the return
        value will be ignored) although the wrapped method is called with the
        passed arguments. So you can validate the inputs should you choose to
        before converting to a url

        This can be stacked with the classmethod and staticmethod decorators.
        In this case, the endpoint decorator should wrap the method decorator.
        For example...
        ```python
        class MyRoutClass:
            
            @route.endpoint()
            @staticmethod
            def my_endpoint(resource: str):
                pass
        ```
        """
        # merge parameters from parent object
        path = self.path + normalize_path(path) if path else self.path
        formatters.update(self.formatters)
        default_formatter = default_formatter or self.default_formatter
        def wrapper(func: Callable[[Any], None]) -> rfc3986.URIReference:
            func_params = inspect.signature(func).parameters
            validate_method_signature(func_params)
            @functools.wraps(func)
            def build_url(*args, **kwargs) -> rfc3986.URIReference:
                # check that all required parameters were passed
                func(*args, **kwargs)
                # extract all path params with pattern '{<name>}'
                path_params = set(re.findall(r"\{(.[^${}]*)}", path))
                args = list(args)
                interpolated = interpolate_path(
                    path,
                    list(path_params),
                    func_params,
                    args,
                    kwargs
                )
                # convert any remaining args (i.e required query parameters)
                # to kwargs
                convert_to_kwargs(path_params, func_params, args, kwargs)
                # convert kwargs to key-val string per formatters
                formatted = format_query_params(
                    formatters,
                    default_formatter,
                    kwargs
                )
                query_str = '&'.join(formatted)
                if query_str:
                    target = interpolated + '?' + query_str
                else:
                    target = interpolated
                return rfc3986.iri_reference(target).encode()
            return build_url
        return wrapper

    

        
