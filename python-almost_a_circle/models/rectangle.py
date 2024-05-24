#!/usr/bin/python3
"""
    This module defines object class Rectangle
        - Inherits from class Base
"""


from models.base import Base


class Rectangle(Base):
    """
        Attributes:
            - id(int): user-specified. Alternatively
            supplied by inherited instance counter

            - width(int): the width of the rectangle
            - height(int): the height of the rectangle
            - x(int): the horizontal print axis
            - y(int): the vertical print axis
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if isinstance(width, int):
            self.__width = width
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        if isinstance(height, int):
            self.__height = height
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @x.setter
    def x(self, x):
        if isinstance(x, int):
            self.__x = x
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, y):
        if isinstance(y, int):
            self.__y = y
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
