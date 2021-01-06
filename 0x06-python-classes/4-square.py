#!/usr/bin/python3
"""Define class"""


class Square():
    """Instantiation of a private attribute"""
    def __init__(self, size=0):
        self.__size = size

    """Getter size"""
    @property
    def size(self):
        return self.__size

    """Setter size"""
    @size.setter
    def size(self, value):
        self.__size = value
        if(type(value)) is not int:
            raise TypeError("size must be an integer")
        if(value) < 0:
            raise ValueError("size must be >= 0")

    """Area of a square"""
    def area(self):
        return int(self.__size) ** 2
