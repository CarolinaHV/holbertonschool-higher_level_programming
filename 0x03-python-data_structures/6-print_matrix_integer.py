#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        esp = ''
        for column in row:
            print("{:s}{:d}".format(esp, column), end="")
            esp = ' '
        print('')
