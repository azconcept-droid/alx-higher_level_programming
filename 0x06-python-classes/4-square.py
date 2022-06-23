#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """An object representing a square"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get and Set size of the square."""
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size
