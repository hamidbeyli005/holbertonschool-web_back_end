#!/usr/bin/env python3
"""
    Type-annotated function safe_first_element that takes a sequence
    seq of any type and returns its first element.
"""
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Gets first element safely.
    """
    if lst:
        return lst[0]
    else:
        return None
