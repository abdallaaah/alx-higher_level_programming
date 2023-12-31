#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return []
    m = matrix.copy()
    for i in range(len(matrix)):
        m[i] = list(map(lambda x: x ** 2, matrix[i]))
    return m
