#!/usr/bin/python3
""" Import class """
from models.rectangle import Rectangle

""" Square class """


class Square(Rectangle):
    """ Constructor """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width
        return self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """ str method """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """ Square update """
        if args is not None:
            ar = 1
            for arg in args:
                if ar == 1:
                    self.id = arg
                elif ar == 2:
                    self.size = arg
                elif ar == 3:
                    self.x = arg
                elif ar == 4:
                    self.y = arg
                ar += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Square instance to dictionary """
        list_attr = ['id', 'width', 'height', 'x', 'y']
        return {key: getattr(self, key) for key in list_attr}
