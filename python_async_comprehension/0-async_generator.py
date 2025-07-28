#!/usr/bin/env python3
"""This module defines async_generator method"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """This method generates random numbers from 0 - 10"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
