#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.

This module defines a Server class that provides pagination
capabilities on a CSV dataset while being resilient to deletions
in the dataset between queries.
"""

import csv
from typing import Dict, List, Any


class Server:
    """
    Server class to paginate a database of popular baby names.
    The pagination is resilient to deletions from the dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the Server with dataset and indexed_dataset caches."""
        self.__dataset: List[List] | None = None
        self.__indexed_dataset: Dict[int, List] | None = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        The first row (header) is skipped. Subsequent calls
        return the cached dataset instead of reloading it.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create and cache a dictionary mapping dataset index to row.

        Returns:
            Dict[int, List]: Keys are positions in the dataset,
            values are the corresponding rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a page of the dataset with hypermedia-style pagination.

        This method is resilient to deletions: even if some rows
        are removed from the dataset, the pagination remains consistent.

        Args:
            index (int): The start index of the page (0-based).
                         Defaults to 0 if None.
            page_size (int): The number of rows to include in the page.

        Returns:
            Dict[str, Any]: A dictionary containing:
                - "index": The start index of the returned page.
                - "next_index": The index to query for the next page.
                - "page_size": The actual number of rows returned.
                - "data": The list of dataset rows for the page.
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
