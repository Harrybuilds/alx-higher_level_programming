#!/usr/bin/python3
# ==≠======================
# sort the dictionary using sorted()
# loop through the new list returned by sorted()
# print formated data of key: value
# (c) 17 August 2023, Owerri, Imo state
# =========================

def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary)
    for k in new_list:
        print("{:s}: {}".format(k, a_dictionary[k]))
