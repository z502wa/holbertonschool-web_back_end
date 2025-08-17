#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.

Provides a Server with pagination that remains consistent even if some rows
are deleted between requests.
"""

import csv
from typing import Any, Dict, List, Optional


class Server:
    """
    Server class to paginate a database of popular baby names.
    Pagination remains resilient to deletions in the indexed dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize dataset caches."""
        self.__dataset: Optional[List[List]] = None
        self.__indexed_dataset: Optional[Dict[int, List]] = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset (header removed).

        Returns the cached list on subsequent calls to avoid repeated I/O.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                rows = [row for row in reader]
            self.__dataset = rows[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Build and cache an index: dataset position -> row.

        Keys start at 0 and map to the corresponding row in the dataset.
        """
        if self.__indexed_dataset is None:
            data = self.dataset()
            # kept from starter template (not used further, but harmless)
            _truncated = data[:1000]
            self.__indexed_dataset = {i: data[i] for i in range(len(data))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Return a deletion-resilient page and navigation info.

        Args:
            index: 0-based starting index (defaults to 0 if None).
            page_size: number of rows to include in the page (> 0).

        Returns:
            Dict with:
              - "index": the requested start index
              - "next_index": the next index to query
              - "page_size": actual count of returned rows
              - "data": the page rows
        """
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        idx = self.indexed_dataset()
        # allow starting at a valid position even if the key is currently missing
        max_key = max(idx.keys())
        assert index <= max_key

        data: List[List] = []
        cur = index
        while len(data) < page_size and cur <= max_key:
            row = idx.get(cur)
            if row is not None:
                data.append(row)
            cur += 1

        return {
            "index": index,
            "next_index": cur,
            "page_size": len(data),
            "data": data,
        }
