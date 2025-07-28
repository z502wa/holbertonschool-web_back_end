#!/usr/bin/env python3
"""
Module: 7-to_kv
This module provides a function to convert a key and a numeric value into a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Generate a key-value tuple where the value is squared.

    Args:
        k (str): The key.
        v (Union[int, float]): The numeric value to be squared.

    Returns:
        Tuple[str, float]: A tuple of the key and the squared value.
    """
    # Compute square of value and return tuple
    return (k, float(v * v))
