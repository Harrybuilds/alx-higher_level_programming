#!/usr/bin/python3
exempt = 'cC'


def no_c(my_string):
    new_string = ''

    """ my first attempt
    i = 0
    while i < len(my_string) or i == len(mystring):
        if my_string[i] != 'c' or my_string[i] != 'C':
            new_string += my_string[i]
            i += 1"""
    for char in my_string:
        if char not in exempt:
            new_string += char

    return new_string
