#!/usr/bin/python3
"""Define class"""


class Square():
    """Instantiation of a private attribute"""
    def __init__(self, size=0):
        self.__size = size
        if(type(self.__size)) is not int:
            raise TypeError("size must be an integer")
        if(self.__size) < 0:
            raise ValueError("size must be >= 0")
    """Area of a square"""
    def area(self):
        return int(self.__size) ** 2
