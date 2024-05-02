#!/usr/bin/env python3
"""
    Type-annotated function element_length that takes a list of strings lst
    and returns a list of integers representing the lengths of the strings.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of integers representing the lengths of the strings."""
    return [(i, len(i)) for i in lst]
