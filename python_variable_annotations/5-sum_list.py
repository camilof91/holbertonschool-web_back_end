#!/usr/bin/env python3
""" Sum two float numbers """


def sum_list(input_list: list[float]) -> float:
    """
    This function adds two floats and returns the sum.
    Args:
      a: The first float number.
      b: The second float numb  er.
    Returns:
      The sum of a and b.
    """
    a:float = 0.0
    for i in input_list: a += i
    return a
