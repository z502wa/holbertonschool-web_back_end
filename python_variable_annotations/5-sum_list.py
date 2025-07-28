#!/usr/bin/env python3
"""
Module: 5-sum_list
This module provides a function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum all floats in the list and return the total.

    Args:
        input_list (List[float]): List of float numbers.

    Returns:
        float: Sum of all elements in input_list.
    """
    # Use built-in sum to calculate the total
    return sum(input_list)
