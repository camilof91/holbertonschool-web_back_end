#!/usr/bin/env python3
"""This coroutine spawns n concurrent tasks of the wait_random coroutine"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This coroutine spawns n concurrent tasks of the wait_random coroutine,
    each with the specified max_delay. It then gathers the results (delays)
    from these tasks and returns them as a list in ascending order.

    Returns:
        List[float]: A list of delays (float values) in ascending order
                    returned by the spawned wait_random coroutines.
    """
    futures = [wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
