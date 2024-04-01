#!/usr/bin/env python3
"""
Module with index_range function to paginate a dataset
"""


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
