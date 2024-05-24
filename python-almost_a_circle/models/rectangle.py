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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if width <= 0:
            raise ValueError("width must be > 0")
        if isinstance(width, int):
            self.__width = width
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height must be > 0")
        if isinstance(height, int):
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @x.setter
    def x(self, x):
        if x < 0:
            raise ValueError("x must be >= 0")
        if isinstance(x, int):
            self.__x = x
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, y):
        if y < 0:
            raise ValueError("y must be >= 0")
        if isinstance(y, int):
            self.__y = y
        else:
            raise TypeError("y must be an integer")
