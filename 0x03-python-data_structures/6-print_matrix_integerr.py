#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(0, len(matrix)):
        temp = len(matrix[x])
        for y in range(0, temp):
            #print(" Item of array is: ", array_items[i][j])
            print("{}".format(), end=" "  if y != x[-1] else "")
        print()
