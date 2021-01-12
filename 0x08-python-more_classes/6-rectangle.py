#!/usr/bin/python3
""" class Rectangle that defines a rectangle with width and height"""


class Rectangle:
    """Define width and height of rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        result = ((self.__height) * ((self.__width * '#') + '\n'))
        return result[:-1]

    def __repr__(self):
        new_inst = '{self.__class__.__name__}({self.width},{self.height})'\
            .format(self=self)
        return new_inst

    def __del__(self):
        print('Bye rectangle...')
        if self.__width is False or self.__height is False:
            pass
        Rectangle.number_of_instances -= 1
