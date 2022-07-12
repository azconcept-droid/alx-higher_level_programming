#!/usr/bin/python3
"""Docs"""

from models.base import Base


class Rectangle(Base):
    """Docs"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Docs"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Docs"""
        return self.__width

    @width.setter
    def width(self, value):
        """Docs"""
        self.integers_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Docs"""
        return self.__height

    @height.setter
    def height(self, value):
        """Docs"""
        self.integers_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Docs"""
        return self.__x

    @x.setter
    def x(self, value):
        """Docs"""
        self.integers_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Docs"""
        return self.__y

    @y.setter
    def y(self, value):
        """Docs"""
        self.integers_validator("y", value)
        self.__y = value

    def integers_validator(self, name, value):
        """Helper function that validates integers
            Args:
                name (str): name of parameter
                value (int): value of parameter
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name=="height" or name=="width" and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Docs"""
        return self.__width * self.__height

    def display(self):
        """Docs"""
        for y in range(self.__y):
            print(" ")
        for row in range(self.__height):
            for x in range(self.__x):
                    print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Docs"""
        print_id = " ("+str(self.id)+") "
        print_pos = str(self.__x)+"/"+str(self.__y)
        print_dim = " - "+str(self.__width)+"/"+str(self.__height)
        return "[{}]".format(type(self).__name__)+print_id+print_pos+print_dim

    def help_update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that help update method"""
        if id is not None:
            self.id = id
        if width is not None:
            self.__width = width
        if height is not None:
            self.__height = height
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def update(self, *args, **kargs):
        """Update arguments

        Args:
            *args (non-keyworded): 
            **kargs (keyworded):
        """
        if args:
            self.help_update(*args)
        elif kargs:
            self.help_update(**kargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rectangle_to_dict =  {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
        return rectangle_to_dict
