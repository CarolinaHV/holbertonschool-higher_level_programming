#!/usr/bin/python3
"""
This function reads a text file (UTF8)
and prints it to stdout

"""


def read_file(filename=""):
    """Read file"""
    with open(filename, "r") as holb_file:
        print(holb_file.read(), end='')
