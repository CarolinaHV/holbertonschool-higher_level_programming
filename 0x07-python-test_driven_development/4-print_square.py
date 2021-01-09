#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    """Thiis is the function"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for fila in range(size):
        for columna in range(size):
            print('#', end='')
        print()
