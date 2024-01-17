#!/usr/bin/python3

def uppercase(str):
    tobeprinted = ""
    for i in range(len(str)):
        num =  ord(str[i])
        if num in range(97, 123):
            tobeprinted += f"{num - 32:c}"
        else:
            tobeprinted += f"{num:c}"
    print("{:s}".format(tobeprinted))
