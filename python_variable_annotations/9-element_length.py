#!/usr/bin/env python3
"""
Module: 9-element_length
This module provides a function to list each element with its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element and its length.

    Args:
        lst (Iterable[Sequence]): Iterable of sequence objects.

    Returns:
        List[Tuple[Sequence, int]]: List of (element, length) tuples.
    """
    # Generate and return list of (element, length) pairs
    return [(i, len(i)) for i in lst]
