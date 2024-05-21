#!/usr/bin/python3
"""
    This  module defines a Rectangle sub-class, Square.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):

    """
        Class represents a square.

        Attributes:
            width (int): length of the x-axis. Default 0
            height (int): length of the y-axis. Default 0

        Methods:
            area: inherited from Rectangle
                calculates the area of the Square

            integer_validator from BaseGeometry
                - validates input is integer
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
