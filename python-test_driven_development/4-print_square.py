#!/usr/bin/python3

"""
Module for the print_square method.
"""


def print_square(size):
    """
    prints a square gird of specified size
    using '#'

    Parameters:
        size (int): dimensions of the square.

    Raises:
        TypeError: if size is not of type int.
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for k in range(0, size):
            print("#", end='')
        print()
