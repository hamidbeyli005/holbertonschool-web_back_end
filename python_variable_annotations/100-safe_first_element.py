#!/usr/bin/env python3
"""
    Type-annotated function safe_first_element that takes a sequence
    seq of any type and returns its first element.
"""
from typing import Union, Any, Sequence


def safe_first_element(seq: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of the sequence or None if empty."""
    if seq:
        return seq[0]
    else:
        return None
