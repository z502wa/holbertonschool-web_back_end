#!/usr/bin/env python3
"""
Module: 2-measure_runtime
This module provides a function to measure average runtime of wait_n.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure average execution time of wait_n coroutine.

    Args:
        n (int): Number of concurrent coroutines.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average runtime in seconds.
    """
    # Record the start time
    start: float = time.time()
    # Run the wait_n coroutine
    asyncio.run(wait_n(n, max_delay))
    # Record the end time
    end: float = time.time()
    # Calculate total elapsed time
    total: float = end - start
    # Return average elapsed time per coroutine
    return total / n
