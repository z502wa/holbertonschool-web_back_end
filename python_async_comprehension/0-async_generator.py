#!/usr/bin/env python3
"""
Module: 0-async_generator
This module defines an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generate 10 random numbers between 0 and 10,
    waiting 1 second between each generation.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
