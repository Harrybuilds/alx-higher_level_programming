#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary.items(),
                      key=lambda x:x)
    #new_list is now a list of tuples(key,value)

    new_dict = dict(new_list)

    for k,v in new_dict.items():
        print("{:s}: {}".format(k, v))
