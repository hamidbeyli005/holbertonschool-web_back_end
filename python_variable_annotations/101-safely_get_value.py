#!/usr/bin/env python3
"""
    Type-annotated function safely_get_value that takes a dict
    and a key as arguments and returns the value of the key.
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Gets value safely."""
    if key in dct:
        return dct[key]
    else:
        return default
