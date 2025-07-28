#!/usr/bin/env python3
"""This module defines measure_runtime"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This method measures the run time tasks completion"""

    start = time()
    tasks = [async_comprehension(), async_comprehension(),
             async_comprehension(), async_comprehension()]
    result = await asyncio.gather(*tasks)
    end = time()
    runTime = end - start
    return runTime
