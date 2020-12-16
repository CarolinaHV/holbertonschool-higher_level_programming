#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    cont = 0
    esp = ''
    for row in matrix:
        for column in row:
            if cont == len(row):
                print("{:s}{:d}".format(esp, column), end="")
            else:
                print("{:s}{:d}".format(esp, column), end="")
            cont += 1
        print(' ')
