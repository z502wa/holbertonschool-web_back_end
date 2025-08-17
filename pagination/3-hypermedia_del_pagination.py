#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.

Provides a Server class that paginates a CSV dataset while remaining resilient
to deletions from the indexed dataset between requests. The returned structure
includes the requested start index, next index to query, the page size actually
returned, and the page data itself.
"""

import csv
import math  # kept per starter template (not strictly required)
from typing import Any, Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: List[List[str]] | None = None
        self.__indexed_dataset: Dict[int, List[str]] | None = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset (header row removed)."""
        if self.__dataset is None:
            with open(self.DATA_FILE, mode="r", newline="") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # kept per starter (not used, but present in the template)
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int | None = None,
                        page_size: int = 10) -> Dict[str, Any]:
        """
        Return a deletion-resilient page and navigation info.

        Args:
            index (int | None): requested start index (0-based). If None, 0.
            page_size (int): desired number of items in the page (> 0).

        Returns:
            Dict[str, Any]: {
                "index": requested start index (int),
                "next_index": next index to query (int),
                "page_size": number of items actually returned (int),
                "data": page rows (List[List[str]])
            }
        """
        # defaults & validations
        if index is None:
            index = 0
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        if not indexed:
            # empty dataset edge-case
            return {"index": index, "next_index": index, "page_size": 0, "data": []}

        max_key = max(indexed.keys())
        # index must be within allowable range even if that key is currently missing
        assert index <= max_key

        # collect up to page_size existing rows, skipping deleted indices
        data: List[List[str]] = []
        cursor = index
        while len(data) < page_size and cursor <= max_key:
            item = indexed.get(cursor)
            if item is not None:
                data.append(item)
            cursor += 1

        next_index = cursor  # first index after the last inspected slot

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
