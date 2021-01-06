#!/usr/bin/python3
"""Define class"""


class Square():
    """Instantiation of a private attribute"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    """Getter position"""
    def position(self):
        return self.__position

    """Setter position"""
    def position(self, value):
        self.__position = value
        if(type(value)) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    """Area of a square"""
    def area(self):
        return int(self.__size) ** 2

    """Print in stdout the square with character"""
    def my_print(self):
        for x in range(self.__position[1]):
            print()
        for f in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end='')
            for c in range(self.__size):
                print("#", end='')
            print()
        """Print a empty line"""
        if(self.__size) == 0:
            print()
