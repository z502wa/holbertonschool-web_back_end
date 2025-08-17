#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.

This module defines a Server class that paginates a CSV dataset of
popular baby names and ensures that pagination remains consistent
even when rows are deleted between queries.
"""

import csv
from typing import Dict, List


class Server:
    """
    Server class to paginate a database of popular baby names.
    Pagination is resilient to deletions in the dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize dataset caches for pagination."""
        self.__dataset: List[List] = []
        self.__indexed_dataset: Dict[int, List] = {}

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        The first row (header) is skipped.
        Subsequent calls return the cached data.
        """
        if not self.__dataset:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return the dataset indexed by position, starting at 0.

        Returns:
            Dict[int, List]: mapping of dataset index to row.
        """
        if not self.__indexed_dataset:
            data = self.dataset()
            self.__indexed_dataset = {i: data[i] for i in range(len(data))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page of the dataset with deletion-resilient pagination.

        Args:
            index (int): The start index of the page (0-based).
                         Defaults to 0 if None.
            page_size (int): Number of rows in the page (> 0).

        Returns:
            Dict: {
                "index": start index of the page,
                "next_index": index to query next,
                "page_size": number of rows returned,
                "data": the page rows
            }
        """
        if index is None:
            index = 0

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        dataset_indexed = self.indexed_dataset()
        max_key = max(dataset_indexed.keys())
        assert index <= max_key

        data: List[List] = []
        current = index
        while len(data) < page_size and current <= max_key:
            if current in dataset_indexed:
                data.append(dataset_indexed[current])
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data,
        }
