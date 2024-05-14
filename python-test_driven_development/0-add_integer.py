#!/usr/bin/python3
"""
Module for add_integer method.
"""


def add_integer(a, b=98):
    """
    Adds two integers together.

    Parameters:
        a (int): the first integer to add.
        b (int, optional): the second integer to add. Defaults to 98.

    Raises:
        TypeError: TypeError: if a or b is not an int.

    Returns:
    int: the sum of a and b.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
