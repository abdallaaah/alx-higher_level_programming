#!/usr/bin/python3
"""test develmopment"""


def matrix_divided(matrix, div):
    """is the matrix divide function
    Args:
    matrix(list): list of matxirx
    div(int): divide numbers
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return divided_matrix
