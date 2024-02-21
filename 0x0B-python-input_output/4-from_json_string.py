#!/usr/bin/python3
import json

"""
module that houses a function that
returns the python objects from a json string
"""


def from_json_string(my_str):
    """
    from_json_string - function to return
    python object from json string

    Args:
       my_str: string to be converted to python object

    Return:
       python object converted from json string
    """

    return json.loads(my_str)
