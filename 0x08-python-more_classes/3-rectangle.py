#!/usr/bin/python3
"""An empty class Rectangle that defines a rectangle"""


class Rectangle:
    """A rectangle object"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area"""

        return (self.__height * self.__width)

    def perimeter(self):
        """Returns rectangle perimeter"""

        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            display = []
            for i in range(self.__height):
                col = ""
                for j in range(self.__width):
                    col += "#"
                display.append(col)
            return "\n".join(display)