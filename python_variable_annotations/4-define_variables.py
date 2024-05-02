#!/usr/bin/env python3
"""
    Type-annotated function define_variables that takes no arguments.
    Returns three variables with specified values.
"""


def define_variables() -> tuple:
    """Return a tuple of three variables."""
    a: int = 1
    b: float = 2.0
    c: str = "string"
    return a, b, c
