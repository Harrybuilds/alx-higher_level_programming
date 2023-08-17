#!/usr/bin/python3

# --------------------------------------------
# if my_list argument is not None

# using map function, pass the lambda function to
# return result of each value multiplied by the
# given number or default number arg value = 0
# and the iterable on which the lambda
# function is to be carried out

# get an identifier to point at the newly
# gerenated list then return the new list
#
# (c) 17, August 2023, Owerri, Imo state
# ---------------------------------------------


def multiply_list_map(my_list=[], number=0):
    if my_list is not None:
        new_list = list(map(lambda x: x*number, my_list))
        return new_list
