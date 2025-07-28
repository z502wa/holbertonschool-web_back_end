#!/usr/bin/env python3
"""
Module: 2-measure_runtime
This module measures the runtime of four parallel async comprehensions.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel and measure total time.

    Returns:
        float: Total runtime in seconds.
    """
    start: float = time.time()
    # Run four async comprehensions concurrently
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    # Calculate and return elapsed time
    return time.time() - start
