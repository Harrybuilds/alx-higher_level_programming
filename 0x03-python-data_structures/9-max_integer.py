#!/usr/bin/python3

def max_integer(my_list=[]):
    max_number = None
    if my_list is not None:
        for i in my_list:
            if max_number is None:
                max_number = i
            elif i > max_number:
                max_number = i

    return max_number
