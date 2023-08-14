#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        """
        used the commented method below,
        but checks were failing until
        i used list unpacking
        x = " ".join(map(lambda x: "{}".format(x), matrix[i]))
        """
        x = matrix[i]
        print(*x)
