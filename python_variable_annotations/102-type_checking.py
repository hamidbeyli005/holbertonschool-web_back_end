#!/usr/bin/env python3
"""
    Type-annotated function type_checking that takes a variable x,
    and returns the type of x.
"""
from typing import Union, Tuple, List, Any


def type_checking(var: Any) -> Tuple[Union[str, List[str]], Any]:
    """Return the type of the variable."""
    return (str(type(var)), var)
