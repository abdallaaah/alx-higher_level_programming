#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        temp = len(matrix[x])
        for y in range(temp):
            print("{}".format(matrix[x][y]), end=" " if y != temp - 1 else "")
        print("\n")
