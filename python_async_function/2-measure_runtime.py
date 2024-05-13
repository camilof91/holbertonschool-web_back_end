#!/usr/bin/env python3
"""Calculates the average execution
time per call to wait_n"""
import asyncio
import time
from . import wait_n
# Assuming wait_n is in the same directory (adjust path if needed)


async def measure_time(num_tasks: int, max_delay: float) -> float:
    """
    Measures the total execution time
    for calling wait_n and returns the average time per call.

    Args:
        num_tasks (int): The number of tasks to spawn in the wait_n coroutine.
        max_delay (float): The upper limit for the random delay in seconds
        used by each wait_random coroutine spawned by wait_n.

    Returns:
        float: The average execution
        time per call to wait_n (total time / num_tasks).
    """
    start_time = time.perf_counter()
    await asyncio.run(wait_n(num_tasks, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time) / num_tasks
