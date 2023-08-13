#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        x = " ".join(map(str, matrix[i]))
        print("{}".format(x))
