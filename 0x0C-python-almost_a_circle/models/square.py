#!/usr/bin/python3
"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializing square class

            Args:
                size: sixe of square
                x: coordinate x
                y: coordinate y
                id: number of objects created
        """
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
        pout = '[{}] ({}) {}/{} - {}'
        idd, xx, yy, siz = self.id, self.x, self.y, self.__size

        return pout.format(type(self).__name__, idd, xx, yy, siz)

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

    def to_dictionary(self):
        """returns the dictionary representation of a square"""
        square_to_dict = dict()
        square_to_dict['size'] = self.__size
        square_to_dict['id'] = self.id
        square_to_dict['x'] = self.x
        square_to_dict['y'] = self.y

        return square_to_dict
