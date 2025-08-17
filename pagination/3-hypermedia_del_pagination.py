#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server with dataset caches."""
        self.__dataset: List[List] | None = None
        self.__indexed_dataset: Dict[int, List] | None = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset (with header row removed).
        Loads the dataset from CSV file on first access and caches it.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return the dataset indexed by position, starting at 0.
        The dataset is cached after first access.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a page of the dataset with deletion-resilient hypermedia pagination.

        Args:
            index (int): The start index of the page. Defaults to 0 if None.
            page_size (int): Number of items per page.

        Returns:
            Dict[str, Any]: {
                "index": current start index,
                "next_index": index to query after this page,
                "page_size": length of the returned data,
                "data": the dataset page
            }
        """
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        max_key = max(indexed.keys())
        assert index <= max_key

        data: List[List] = []
        current = index

        while len(data) < page_size and current <= max_key:
            if current in indexed:
                data.append(indexed[current])
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data,
        }
