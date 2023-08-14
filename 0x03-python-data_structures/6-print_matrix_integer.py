#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        #        x = " ".join(map(lambda x: "{}".format(x), matrix[i]))
        x = matrix[i]
        #       xprint("{:d}".format(*x))
        print(*x)
