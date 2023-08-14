#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        x = " ".join(map(lambda x: "{}".format(x), matrix[i]))
        print("{}".format(x))
