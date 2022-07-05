#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square inherited from Rectangle."""

    def __init__(self, size):
        """Intialize a square.
        Args:
            size (int): sizeof square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
