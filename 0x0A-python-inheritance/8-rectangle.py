#!/usr/bin/python3
"""
Create a BaseGeometry class

"""


class BaseGeometry:
    """Public instance method"""
    def area(self):
        """Raise exception message"""
        raise Exception('area() is not implemented')

    """Public instance method"""
    def integer_validator(self, name, value):
        """Validation value"""
        if type(value) is not int:
            """Raise exception message"""
            raise TypeError("{:s} name must be an integer".format(name))
        if value <= 0:
            """Raise exception message"""
            raise ValueError('{:s} name must be greater than 0'.format(name))


"""
Create a Rectangle subclass
inherit from BaseGeometry class
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height