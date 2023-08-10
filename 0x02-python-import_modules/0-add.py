#!/usr/bin/python3
import add_0 as ad

add = ad.add
a = 1
b = 2
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
