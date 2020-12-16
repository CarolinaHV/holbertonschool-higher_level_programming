#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    cont = 0
    for row in matrix:
        for column in row:
            if cont == len(row) - 1:
                print("{:d}".format(column), end="")
            else:
                print("{:d}".format(column), end="")
            cont += 1
        print('')
