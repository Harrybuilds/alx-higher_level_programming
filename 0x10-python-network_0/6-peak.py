#!/usr/bin/env python3
"""
 function to findthepeak number in a list
"""
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    mid = len(list_of_integers) // 2
    if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
