#!/usr/bin/env python3
"""
This function takes an iterable of sequences (e.g., lists, tuples, strings)
and returns a list of tuples.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function iterates through an iterable of sequences and calculates
    the length of each sequence. It then returns a list of tuples where each
    tuple contains the original sequence and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences of elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
