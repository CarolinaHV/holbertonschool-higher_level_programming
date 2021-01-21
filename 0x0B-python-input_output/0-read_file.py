#!/usr/bin/python3
"""
This function reads a text file (UTF8)
and prints it to stdout

"""


def read_file(filename=""):
    with open(filename) as file:
        print(file.read(), end='')
