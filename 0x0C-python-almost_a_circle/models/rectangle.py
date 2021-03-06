#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """Initialize new rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x-axis position of rectangle
            y (int): y-axis position of rectangle
            id (int): identity of rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle.
        Args:
            value (int): value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle
        Args:
            value (int): value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Get x position of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x position of rectangle
        Args:
            value (int): value of x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y position of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Set y position of rectangle
        Args:
            y (int): value of y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute the area of rectangle class"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle class shape"""
        for y in range(self.__y):
            print(" ")
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """Print rectangle to stdout
        Returns:
            string representation of object
        """
        print_id = " ("+str(self.id)+") "
        print_pos = str(self.__x)+"/"+str(self.__y)
        print_dim = " - "+str(self.__width)+"/"+str(self.__height)
        return "[{}]".format(type(self).__name__)+print_id+print_pos+print_dim

    def help_update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that help update method
        Args:
            id (int): identity of object
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x position of rectangle
            y (int): y position of rectangle
        """
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
            *args (non-keyworded): no keyword arguments
            **kargs (keyworded): keyword arguments
        """
        if args:
            self.help_update(*args)
        elif kargs:
            self.help_update(**kargs)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rectangle_to_dict = dict()

        rectangle_to_dict['x'] = self.__x
        rectangle_to_dict['y'] = self.__y
        rectangle_to_dict['id'] = self.id
        rectangle_to_dict['height'] = self.__height
        rectangle_to_dict['width'] = self.__width

        return rectangle_to_dict
