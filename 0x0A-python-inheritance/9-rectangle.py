#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle inherited from BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate area of rectangle"""

        Area = self.__width * self.__height
        return Area

    def __str__(self):
        """Print object to stdout"""

        display_rect = "[" + self.__class__.__name__ + "]"
        display_rect += " " + str(self.__width) + "/" + str(self.__height)
        return display_rect
