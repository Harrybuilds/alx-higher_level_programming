#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[0 : x]
        for element in new_list:
            print("{:d}".format(element), end="")
            if element is new_list[-1]:
                print()
        last_digit = new_list[-1]
        return last_digit
    except ValueError:
        return
