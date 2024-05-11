#!/usr/bin/env python3
""" Sum list numbers """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a number by a given multiplier.

    Args:
        multiplier (float): The value to use for multiplication.

    Returns:
        Callable[[float], float]: A new function that
        takes a float and returns its product with the multiplier.
    """
    return lambda x: x * multiplier
