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

    def __init__(self, size=0):
        """
        Initialize new Square instance.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method calculates the area of instance Square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Method prints instance of Square
        represented by '#'.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for k in range(0, self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
