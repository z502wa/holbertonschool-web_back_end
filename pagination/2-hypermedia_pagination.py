#!/usr/bin/env python3
"""
Hypermedia pagination module.

This module exposes a Server class that paginates a CSV dataset of popular
baby names and returns hypermedia-style metadata for each requested page.
All functions are type-annotated and documented.
"""

import csv
import math
from typing import Any, Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute the start and end indexes (slice bounds) for a given page.

    The page number is 1-indexed. The returned tuple can be used directly
    to slice a list without further adjustments.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple (start_index, end_index).
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server with a lazy, cached dataset."""
        self.__dataset: List[List[str]] | None = None

    def dataset(self) -> List[List[str]]:
        """
        Return the cached dataset (header removed).

        The dataset is loaded from CSV on the first access and then cached
        to avoid repeated disk reads.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, mode="r", newline="") as f:
                reader = csv.reader(f)
                rows: List[List[str]] = [row for row in reader]
            # Skip the header row
            self.__dataset = rows[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return a single page of the dataset.

        Args:
            page (int): 1-indexed page number. Must be > 0.
            page_size (int): Number of items per page. Must be > 0.

        Returns:
            List[List[str]]: The list of rows for the requested page.
                             If the page is out of range, returns [].
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return hypermedia pagination metadata and the page data.

        The method reuses get_page to fetch the data and then computes
        the appropriate metadata values.

        Args:
            page (int): 1-indexed page number.
            page_size (int): Number of items per page.

        Returns:
            Dict[str, Any]: A dictionary with keys:
                - "page_size": length of the returned page (int)
                - "page": current page number (int)
                - "data": the page data (List[List[str]])
                - "next_page": next page number or None
                - "prev_page": previous page number or None
                - "total_pages": total number of pages (int)
        """
        # Reuse get_page (also validates inputs with asserts).
        page_data: List[List[str]] = self.get_page(page, page_size)

        total_items: int = len(self.dataset())
        total_pages: int = math.ceil(total_items / page_size)

        page_size_actual: int = len(page_data)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size_actual,
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
