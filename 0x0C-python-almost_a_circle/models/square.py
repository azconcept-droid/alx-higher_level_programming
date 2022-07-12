#!/usr/bin/python3
"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Docs"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of the square.
        Args:
            value (int): value of size
        """
        self.integers_validator("width", value)
        self.__width = value
        self.__height = value

    def __str__(self):
        return '[{}] ({}) {}/{} - {}' \
        .format(type(self).__name__, self.id, self.x, self.y, self.width)

    def help_update(self, id=None, size=None, x=None, y=None):
        """Internal method that help update method"""
        if id is not None:
            self.id = id
        if size is not None:
            self.__size = size
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
        else:
            self.help_update(**kargs)
