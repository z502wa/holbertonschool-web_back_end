#!/usr/bin/env python3
"""
Module: 1-concurrent_coroutines
This module provides a coroutine to run wait_random n times.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times concurrently with given max_delay.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay to pass to wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create tasks for wait_random(max_delay)
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    results: List[float] = []
    # Gather results as they complete (ascending order)
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
