#!/usr/bin/python3
# ------------------------
# use dict comprehension to create a new dict
# while multiplying the dict value by 2
#
# get an identifier to point to the new dict
#
# return the new dictionary
# ------------------------

def multiply_by_2(a_dictionary):
    new_dict = {k: v*2 for k, v in a_dictionary.items()}
    return new_dict
