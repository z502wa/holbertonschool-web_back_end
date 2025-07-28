#!/usr/bin/env python3
"""
Module: 6-sum_mixed_list
This module provides a function to sum a list of ints and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum all integers and floats in the list and return the total as a float.

    Args:
        mxd_lst (List[Union[int, float]]): List of integers and floats.

    Returns:
        float: Sum of all elements in mxd_lst.
    """
    # Calculate the sum of mixed numeric list and return as float
    return float(sum(mxd_lst))
