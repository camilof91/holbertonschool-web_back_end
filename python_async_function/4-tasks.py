#!/usr/bin/env python3
"""Spawns multiple wait_random coroutines
concurrently and returns the results."""
from typing import List
import asyncio
from . import (
    task_wait_random,
)  # Assuming task_wait_random is in the same directory (adjust path if needed)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple task_wait_random
    coroutines concurrently and returns the results.

    Args:
        n (int): The number of tasks to spawn concurrently.
        max_delay (int): The upper limit for the random delay in seconds
                           used by each wait_random coroutine within the tasks.

    Returns:
        List[float]: A list containing the delay values (float) returned by all
        concurrent wait_random calls.
    """
    tasks = [asyncio.create_task(
        task_wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results
