#!/usr/bin/env python3
"""
Module: 1-async_comprehension
This module defines a coroutine that collects random numbers
using an asynchronous comprehension over async_generator.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator.

    Uses an asynchronous comprehension to gather the values.

    Returns:
        List[float]: A list of 10 random floats.
    """
    # Perform async comprehension to collect values as they are yielded
    return [i async for i in async_generator()]
