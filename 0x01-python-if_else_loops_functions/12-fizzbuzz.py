#!/usr/bin/python3

def fizzbuzz():
    i = 1

    while i != 101:
        if i % 15 == 0:
            print("{}".format("FizzBuzz"), end=' ')
        elif i % 5 == 0:
            print("{}".format("Buzz"), end=' ')
        elif i % 3 == 0:
            print("{}".format("Fizz"), end=' ')
        else:
            print("{}".format(i), end=' ')
        i += 1
