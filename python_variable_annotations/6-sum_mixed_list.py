#!/usr/bin/env python3
""" Sum list numbers """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of a list of floats.

    Args:
        input_list: A list of floating-point numbers.

    Returns:
        float: The sum of all elements in the list.
    """
    total: float = 0.0
    for num in mxd_lst:
        total += num
    return total
