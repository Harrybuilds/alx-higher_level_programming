#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return
    new_list = my_list[0:x]
    for element in new_list:
        try:
            print("{:d}".format(element), end="")
            if element is new_list[-1]:
                print()
        except ValueError:
            continue
        except TypeError:
            continue
    last_digit = new_list[-1]
    return last_digit
