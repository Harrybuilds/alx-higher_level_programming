#!/usr/bin/python3
"""
 function to findthepeak number in a list
"""


def find_peak(numbr):
    '''
        Finds the peak in a list of numbers
    '''
    lengt = len(numbr)
    if lengt == 0:
        return None
    if lengt == 1:
        return (numbr[0])
    if lengt == 2:
        return numbr[0] if numbr[0] >= numbr[1] else numbr[1]

    for idx in range(0, lengt):
        value = numbr[idx]
        if (idx > 0 and idx < lengt - 1 and
                numbr[idx + 1] <= value and numbr[idx - 1] <= value):
            return value
        elif idx == 0 and numbr[idx + 1] <= value:
            return value
        elif idx == lengt - 1 and numbr[idx - 1] <= value:
            return value
    return pick
