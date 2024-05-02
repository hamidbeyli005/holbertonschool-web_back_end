#!/usr/bin/env python3
"""
    Type-annotated function safely_get_value that takes a dict
    and a key as arguments and returns the value of the key.
"""
from typing import Union, Any, Mapping


def safely_get_value(dct: Mapping, key: Any, default: Union[None, str] = None) -> Union[Any, Union[str, None]]:
    """Return the value of the key in the dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
