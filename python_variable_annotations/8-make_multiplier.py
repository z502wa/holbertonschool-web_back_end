#!/usr/bin/env python3
"""
Module: 8-make_multiplier
This module provides a function to create a multiplication function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies its input by multiplier.

    Args:
        multiplier (float): The factor to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
                                  the product as float.
    """
    # Define the multiplier function
    def multiplier_func(value: float) -> float:
        """
        Multiply input value by the outer multiplier.

        Args:
            value (float): The number to multiply.

        Returns:
            float: Result of multiplication.
        """
        # Multiply value by multiplier
        return value * multiplier

    return multiplier_func
