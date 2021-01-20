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


"""
Create a Rectangle subclass
inherit from BaseGeometry class
"""


class Rectangle(BaseGeometry):
    """inherits of BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implementation method calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

"""
Square class
inherits from Rectangle

"""


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implementation method calculate area"""
        return self.__size * self.__size

    def __str__(self):
        """square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
