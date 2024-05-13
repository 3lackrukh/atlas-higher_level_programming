#!/usr/bin/python3

"""
Module defines geometric class Square.
"""


class Square:
    """
    Class represents a square.

    Attributes:
        size (int): length of the sides.
        position (tuple): position adjustment in 2-d space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize new Square instance.
        """

        self.size = size 
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value) or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                        print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print()

