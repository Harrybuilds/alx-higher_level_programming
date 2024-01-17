#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("{:s} ".format("FIZZBUZZ"), end="")
        elif i % 5 == 0:
            print("{:s} ".format("BUZZ"), end="")
        elif i % 3 == 0:
            print("{:s} ".format("FIZZ"), end="")
        else:
            print("{:d} ".format(i), end="")
