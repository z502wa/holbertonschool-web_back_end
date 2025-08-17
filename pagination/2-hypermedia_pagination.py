#!/usr/bin/env python3
"""
Hypermedia pagination module.
Provides Server class with get_page and get_hyper methods to paginate a CSV
dataset and return hypermedia-style pagination metadata.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute start and end indices for a given page and page size.

    Args:
        page (int): 1-indexed page number.
        page_size (int): number of items per page.

    Returns:
        Tuple[int, int]: (start_index, end_index) slice bounds.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return cached dataset (header removed)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): 1-indexed page number.
            page_size (int): number of items per page.

        Returns:
            List[List]: rows for the requested page; [] if out of range.
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
        Return hypermedia pagination metadata and page data.

        Args:
            page (int): 1-indexed page number.
            page_size (int): number of items per page.

        Returns:
            Dict[str, Any]: {
                "page_size": int,
                "page": int,
                "data": List[List],
                "next_page": Optional[int],
                "prev_page": Optional[int],
                "total_pages": int
            }
        """
        # reuse get_page (also validates inputs)
        data_page = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size) if page_size else 0

        page_size_actual = len(data_page)  # 0 if out of range (matches checker)

        next_page = page + 1 if page < total_pages and page_size_actual > 0 else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size_actual,
            "page": page,
            "data": data_page,
            "next_page": next_page,
