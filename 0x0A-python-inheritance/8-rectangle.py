#!/usr/bin/python3
"""An empty class that defines a Geometry"""


class BaseGeometry:
    """A BaseGeometry object"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate data

        Args:
            name (str): name of the geometry
            value (int): value of the the geometry
        Raise:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    class Rectangle(BaseGeometry):
        """Rectangle object"""

        def __init__(self, width, height):
            """initialize rectangle class

            Args:
                width (int): width of the geometry
                height (int): height of the the geometry
            """
            integer_validator(name, width)
            integer_validator(name, height)
            self.__width = width
            self.__height = height
