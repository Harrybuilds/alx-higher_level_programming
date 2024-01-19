#!/usr/bin/python3
import add_0 as m
"""add = __import__('add_0.py').add"""

a = 1
b = 2

print("{:d} + {:d} = {:d}".format(a, b, m.add(a, b)))
