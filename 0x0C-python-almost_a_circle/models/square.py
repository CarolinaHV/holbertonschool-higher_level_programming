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
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, 
                                                 self.size)

    def update(self, *args, **kwargs):
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
        dic_s = {}
        dic_s = dict(id = self.id)
        dic_s = dict(size = self.size)
        dic_s = dict(x = self.x)
        dic_s = dict(y = self.y)
        return dic_s

