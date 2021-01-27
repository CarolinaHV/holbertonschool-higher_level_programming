#!/usr/bin/python3
""" Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ Class rectangle inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        #super().__init__(id)

    """ Getters """
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    """ Setters """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    
    def area(self):
        return (self.width * self.height)


    def display(self):
        print ((self.__y * '\n'), end='')
        print ((self.__x * ' ' + '#' * self.__width + '\n') * (self.__height),
               end='')


    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)


    def update(self, *args, **kwargs):
        if args is not 0:
            ar = 1
            for arg in args:
                if ar == 1:
                    Base.__init__(self, arg)
                elif ar == 2:
                    self.__width = arg
                elif ar == 3:
                    self.__height = arg
                elif ar == 4:
                    self.__x = arg
                elif ar == 5:
                    self.__y = arg
                ar += 1
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        dic = {}
        dic = dict(id = self.id)
        dic = dict(width = self.width)
        dic = dict(height = self.height)
        dic = dict(x = self.x)
        dic = dict(y = self.y)
        return dic
