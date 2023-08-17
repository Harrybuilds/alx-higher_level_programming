#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary.items(),
                      key=lambda x: x)
    new_dict = dict(new_list)

    for k, v in new_dict.items():
        print(k, ": ", v)
