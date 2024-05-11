#!/usr/bin/python3

"""
Module defines geometric class Square.
"""


class Square:
    """
    Class represents a square.
    
    Attributes:
        size (int): length of the sides.
    """

    def __init__(self, size):
        """
        Initialize new Square instance.
        """
        self.__size = size
