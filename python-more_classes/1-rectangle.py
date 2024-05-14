#!/usr/bin/python3

"""
Module defines geometric class Rectangle.
"""


class Rectangle:
    """
    Class represents a Rectangle.

    Attributes:
        width (int): length of the x-axis. Default 0
        height (int): length of the y-axis. Default 0

    Raises:
        TypeError: if height or width are not type int.
        ValueError: if height or width are not of type int.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize new Rectangle instance.
        """
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__height = height
        self.__width = width
