#!/usr/bin/env python3
"""This coroutine waits for a random delay """
import asyncio
import random


async def wait_random(max_delay: float = 10.0) -> float:
    """
    This coroutine waits for a random delay between 0 and the specified
    max_delay (inclusive) seconds and then returns the delay value.

    Args:
        max_delay (float, optional): The upper limit
        for the random delay in seconds. Defaults to 10.0.

    Returns:
        float: The random delay that the coroutine waited for.
    """
    delay = random.uniform(0, max_delay)
    # Generate random delay between 0 and max_delay
    await asyncio.sleep(delay)
    # Wait for the random delay asynchronously
    return delay
