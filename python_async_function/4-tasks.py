#!/usr/bin/env python3
"""
Module: 4-tasks
This module provides a coroutine to run task_wait_random n times.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times concurrently with given max_delay.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order.
    """
    # Create tasks using task_wait_random(max_delay)
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results: List[float] = []
    # Collect results as tasks complete (ascending order)
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
