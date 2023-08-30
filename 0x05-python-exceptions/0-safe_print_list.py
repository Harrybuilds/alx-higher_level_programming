#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new_list = my_list[0:x]
    i = 0
    while i < x:
        try:
            print("{:d}".format(new_list[i]), end="")
            if new_list[i] is new_list[-1]:
                print()
        except (ValueError, TypeError, IndexError):
            break
        i += 1
    last_digit = new_list[-1]
    return last_digit
