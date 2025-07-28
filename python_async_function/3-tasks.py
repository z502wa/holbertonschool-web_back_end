#!/usr/bin/env python3
"""
Module: 3-tasks
This module provides a function to create an asyncio Task.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task from wait_random coroutine.

    Args:
        max_delay (int): The max delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The created Task object.
    """
    # Schedule the wait_random coroutine as an asyncio Task
    return asyncio.create_task(wait_random(max_delay))
