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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Docs"""
        return self.__height

    @height.setter
    def height(self, value):
        """Docs"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Docs"""
        return self.__x

    @x.setter
    def x(self, value):
        """Docs"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Docs"""
        return self.__y

    @y.setter
    def y(self, value):
        """Docs"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

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
        return "[Rectangle]"+print_id+print_pos+print_dim

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
        """Docs"""
        if args:
            self.help_update(*args)
        else:
            self.help_update(**kargs)
