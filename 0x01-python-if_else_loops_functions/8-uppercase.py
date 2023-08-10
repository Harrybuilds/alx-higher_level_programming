#!/usr/bin/python3

def uppercase(str):
    return_string = ''
    i = 0
    ascii_offset = ord('a') - ord('A')

    while i != len(str):
        if str[i] < 'a' or str[i] > 'z':
            print("{}".format(str[1]))
            i += 1
        else:
            uppercase = chr(ord(str[i]) - ascii_offset)
            print("{}".format(uppercase))
            i += 1
