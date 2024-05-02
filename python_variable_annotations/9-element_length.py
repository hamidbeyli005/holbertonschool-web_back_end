#!/usr/bin/env python3
"""
    Type-annotated function element_length that takes a list lst of strings
    and returns a list of integers representing the lengths of the strings.
"""
from typing import List


def element_length(lst: List[str]) -> List[int]:
    """Return a list of integers representing the lengths of the strings."""
    return [len(i) for i in lst]
