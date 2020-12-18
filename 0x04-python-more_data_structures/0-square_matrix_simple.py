#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(lambda i: i * i, matrix[i])))
    return new_matrix
