#!/usr/bin/python3

def weight_average(my_list=[]):
    total_weight = 0
    average_weight = 0
    for tup in my_list:
        average_weight += tup[1]
        total_weight += (tup[0] * tup[1])
    return total_weight / average_weight
