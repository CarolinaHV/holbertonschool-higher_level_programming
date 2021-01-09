#!/usr/bin/python3
"""Function divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """This is the function"""
    new_list = []
    new_row = []

    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error1)
        if len(matrix[0]) != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        if div == 0:
            raise ZeroDivisionError('division by zero')
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(error1)
            division = round(x / div, 2)
            new_row.append(division)
        new_list.append(new_row)
    return new_list
