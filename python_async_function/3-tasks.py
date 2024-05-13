#!/usr/bin/env python3
"""Creates an asyncio
task that calls wait_random."""
import asyncio
from . import (
    wait_random,
)  # Assuming wait_random is in the same directory (adjust path if needed)


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task that calls wait_random.

    Args:
        max_delay (int): The upper limit for the random delay in seconds
                           used by the wait_random coroutine within the task.

    Returns:
        asyncio.Task: The task
        object that will asynchronously call wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
