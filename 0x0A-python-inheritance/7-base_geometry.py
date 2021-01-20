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
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            """Raise exception message"""
            raise ValueError('{:s} must be greater than 0'.format(name))
