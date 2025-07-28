#!/usr/bin/env python3
"""
Asynchronously yield 10 random floats between 0 and 10,
waiting 1 second between each yield.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield 10 random floats in [0, 10], pausing 1 second each time.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
