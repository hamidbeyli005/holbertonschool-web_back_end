#!/usr/bin/env python3
"""
    Type-annotated coroutine that will collect a list of delays.
"""

from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for a random delay and returns a list delay"""
    tasks = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(tasks)
