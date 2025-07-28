#!/usr/bin/env python3
"""
Module: 0-basic_async_syntax
This module defines an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds (inclusive).

    Args:
        max_delay (int): The upper bound for the random delay in seconds.

    Returns:
        float: The actual delay that was waited.
    """
    # Generate a random float delay between 0 and max_delay
    delay: float = random.uniform(0, max_delay)
    # Asynchronously sleep for the generated delay
    await asyncio.sleep(delay)
    # Return the actual delay value
    return delay
