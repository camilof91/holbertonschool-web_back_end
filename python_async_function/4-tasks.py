#!/usr/bin/env python3
"""Spawns multiple wait_random coroutines
concurrently and returns the results."""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple task_wait_random
    coroutines concurrently and returns the results.

    Returns:
        List[float]: A list containing the delay values (float) returned by all
        concurrent wait_random calls.
    """
    futures = [task_wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
