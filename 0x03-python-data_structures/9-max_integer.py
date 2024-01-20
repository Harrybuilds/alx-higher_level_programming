#!/usr/bin/python3

def max_integer(my_list=[]):
    """ finds the highest integerin the list
    without using the built-in max()
    """

    return eval(f"max({my_list}) if len(my_list) > 0 else None")
