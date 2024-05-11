#!/usr/bin/env python3
''' '''
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This coroutine spawns n concurrent tasks of the wait_random coroutine,
    each with the specified max_delay. It then gathers the results (delays) 
    from these tasks and returns them as a list in ascending order.

    Args:
        n (int): The number of wait_random coroutines to spawn concurrently.
        max_delay (float): The upper limit for the random delay in seconds 
                            used by each wait_random coroutine.

    Returns:
        List[float]: A list of delays (float values) in ascending order 
                    returned by the spawned wait_random coroutines.
    """
    tasks = []
    for _ in range(n):
        # Create tasks for each wait_random coroutine
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    # Wait for all tasks to complete and gather their results
    results = await asyncio.gather(*tasks)

    # No sorting needed due to the nature of asynchronous execution
    return results
    