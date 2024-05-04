#!/usr/bin/env python3
"""
    Type-annotated coroutine that will be randomly decorated.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay and returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
