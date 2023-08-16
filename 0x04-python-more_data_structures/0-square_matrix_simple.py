#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_list = []

        for item in matrix:
            new = list(map(lambda x: x**2, item))
            new_list.append(new)

        return new_list
