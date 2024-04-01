#!/usr/bin/env python3
"""
Module with index_range function and Server class to paginate a dataset
"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    Returns a tuple containing the start and end indexes
    for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items to display per page.

    Returns:
        tuple: A tuple containing the start and end indexes
               for the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset based on the given page and page_size.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items to display per page.

        Returns:
            List[List]: A list of lists representing the requested page
                        of the dataset.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        try:
            return dataset[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing hypermedia pagination data for the
        requested page of the dataset.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items to display per page.

        Returns:
            Dict: A dictionary containing hypermedia pagination data.
        """
        data = self.get_page(page, page_size)
        total_pages = max(math.ceil(len(self.dataset()) / page_size), 1)

        hypermedia = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }

        return hypermedia
