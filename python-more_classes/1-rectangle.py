#!/usr/bin/python3

"""
Module defines geometric class Rectangle.
"""


class Rectangle:
    """
    Class represents a Rectangle.

    Attributes:
        width (int): length of the x-axis.
        height (int): length of the y-axis.
    """

    def __init__(self, height, width):
        """
        Initialize new Rectangle instance.
        """
        self.__height = height
        self.__width = width
