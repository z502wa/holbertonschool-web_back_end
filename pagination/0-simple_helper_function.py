#!/usr/bin/env python3
"""
This module contains a simple helper function for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing start and end index for pagination parameters
    
    Args:
        page: integer representing the page number (1-indexed)
        page_size: integer representing the number of items per page
    
    Returns:
        tuple: containing start index and end index for the given page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
