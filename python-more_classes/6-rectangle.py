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
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize new Rectangle instance.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        """
        Method calculates the area of instance Rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Method calculates the perimeter of instance Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def print(self):
        """
        Method prints instance of Rectangle
        represented by '#'.
        """
        if self.__area == 0:
            print()
        else:
            for i in range(0, self.__height):
                for k in range(0, self.__width):
                    print("#", end="")
            print()

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            r_mtrx = ""
            for i in range(self.__height - 1):
                r_mtrx += "#" * self.__width + "\n"
            r_mtrx += "#" * self.__width
            return r_mtrx

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
