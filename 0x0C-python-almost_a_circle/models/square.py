#!/usr/bin/python3
"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Docs"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """Get size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square.
        Args:
            value (int): value of size
        """
        self.integers_validator("width", value)
        self.__size = value

    def __str__(self):
        return '[{}] ({}) {}/{} - {}' \
        .format(type(self).__name__, self.id, self.x, self.y, self.__size)

    def help_update(self, id=None, size=None, x=None, y=None):
        """Internal method that help update method"""
        if id is not None:
            self.id = id
        if size is not None:
            self.__size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

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
