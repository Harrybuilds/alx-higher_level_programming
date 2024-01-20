#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ function to print a matrix """

    for r in (matrix):
        for c in r:
            print("{:d}".format(c), end=" " if r.index(c) != len(r) - 1 else "")
        print("{}".format("$"))
