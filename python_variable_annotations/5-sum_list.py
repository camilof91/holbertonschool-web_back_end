#!/usr/bin/env python3
""" Sum list numbers """


def sum_list(input_list: float) -> float:
    """Calculates the sum of a list of floats.

    Args:
        input_list: A list of floating-point numbers.

    Returns:
        float: The sum of all elements in the list.
    """
    total = 0.0
    for num in input_list:
        total += num

    return total