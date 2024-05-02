#!/usr/bin/env python3
"""
    This module contains a function that multiplies a float by a given number.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function returns a function that multiplies a float by a given number.
    """
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
