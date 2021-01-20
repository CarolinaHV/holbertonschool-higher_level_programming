#!/usr/bin/python3
"""
Myint class

"""


class MyInt(int):
    """Function equal"""
    def __ne__(self, other):
        return int.__eq__(self, other)

    """Function no equal"""
    def __eq__(self, other):
        return int.__ne__(self, other)
