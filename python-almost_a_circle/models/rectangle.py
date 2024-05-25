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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Method calculates the area of instance Rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Method prints instance of Rectangle
        represented by '#'.
        """
        if self.area == 0:
            print()
        else:
            for i in range(0, self.y):
                print()
            for i in range(0, self.__height):
                for k in range(0, self.x):
                    print(" ", end="")
                for k in range(0, self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        string = f"[Rectangle] ({self.id})"
        string += f" {self.x}/{self.y} - {self.width}/{self.height}"
        return string

    def update(self, *args):
        args_len = len(args)
        if args_len > 2:
            self.id = args[1]
        if args_len > 3:
            self.width = args[2]
        if args_len > 4:
            self.height = args[3]
        if args_len > 5:
            self.x = args[4]
        if args_len > 6:
            self.y = args[5]
