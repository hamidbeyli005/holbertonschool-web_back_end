#!/usr/bin/env python3
"""
    Type-annotated function type_checking that takes a variable x,
    and returns the type of x.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Zooms in a list by a factor of 2."""
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
