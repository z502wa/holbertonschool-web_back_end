#!/usr/bin/env python3
"""
Module: 7-to_kv
This module provides a function to convert a key and a numeric
value into a key-value tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Generate a key-value tuple where the numeric value is squared.

    Args:
        k (str): The key.
        v (Union[int, float]): The numeric value to square.

    Returns:
        Tuple[str, float]: A tuple containing the key and squared value.
    """
    # Compute square of value and return as tuple
    return (k, float(v * v))
