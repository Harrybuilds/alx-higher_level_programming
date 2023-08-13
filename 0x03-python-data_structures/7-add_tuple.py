#!/usr/bin/python3
lis = [0, 0]


def add_tuple(tuple_a=(), tuple_b=()):
    """
    first convert the tuples to list to enable
    data change and manipulation
    """
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)

    if len(tuple_a) < 2:
        if len(tuple_a) > 0:
            tuple_a.append(0)
        else:
            tuple_a.extend(lis)
    elif len(tuple_a) > 2:
        tuple_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) < 2:
        if len(tuple_b) > 0:
            tuple_b.append(0)
        else:
            tuple_b.extend(lis)
    elif len(tuple_b) > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]

    """return a new tuple after manipulation"""
    return (first, second)
