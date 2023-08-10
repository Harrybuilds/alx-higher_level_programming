#!/usr/bin/python3

def fizzbuzz():
    i = 1

    while i != 100:
        if i % 15 == 0:
            print("{}".format("FIZZ BUZZ"), end=' ')
        elif i % 5 == 0:
            print("{}".format("BUZZ"), end=' ')
        elif i % 3 == 0:
            print("{}".format("FIZZ"), end=' ')
        else:
            print("{}".format(i), end=' ')
        i += 1
