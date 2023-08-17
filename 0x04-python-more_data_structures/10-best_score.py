#!/usr/bin/python3

# -----------------------
# check if argument passed is None
# if yes: return None

# else: set the variables maxi = 0, key = ""

# loop through the keys in dictionary, comparing
# the values to the set highest number
#
# if value greater than highest number, set
# value to be highest number

# return key with the highest number

# (c) 17, August 2023, Owerri, Imo state
# -----------------------

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        maxi = 0
        key = ""

        for k, v in a_dictionary.items():
            if v > maxi:
                maxi = v
                key = k

        return key
