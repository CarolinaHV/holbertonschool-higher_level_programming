#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    cont = 0
    for row in matrix:
        esp = ''
        for column in row:
            if cont == len(row):
                print("{:s}{:d}".format(esp, column), end="")
            else:
                print("{:s}{:d}".format(esp, column), end="")
            cont += 1
        esp = ' '
        print(' ')
