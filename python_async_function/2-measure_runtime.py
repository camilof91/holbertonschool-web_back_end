#!/usr/bin/env python3
"""Calculates the average execution
time per call to wait_n"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n
# Assuming wait_n is in the same directory (adjust path if needed)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time
    for calling wait_n and returns the average time per call.

    Returns:
        float: The average execution
        time per call to wait_n (total time / num_tasks).
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time) / n
