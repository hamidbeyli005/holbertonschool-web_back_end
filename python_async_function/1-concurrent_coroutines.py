#!/usr/bin/env python3
"""
    Type-annotated coroutine that will collect a list of delays.
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Waits for a random delay and returns a list of delays."""
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
