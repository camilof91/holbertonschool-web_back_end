#!/usr/bin/env python3
'''Calculates the start and end index for pagination
'''


def index_range(page: int, page_size: int) -> tuple:
    '''Calculates the start and end index for pagination.

    Args:
        page: The current page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple containing the start (inclusive)
        and end (exclusive) indices for the current page.

    Raises:
        ValueError: If page or page_size is non-positive.
    '''
    start = (page - 1) * page_size
    return (start, start + page_size)