#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key is None:
        del a_dictionary[key]
    return a_dictionary
