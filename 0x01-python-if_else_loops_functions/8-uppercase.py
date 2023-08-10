#!/usr/bin/python3

def uppercase(str):
    return_string = ''
    i = 0
    ascii_offset = ord('a') - ord('A')

    while i != len(str):
        if str[i] < 'a' or str[i] > 'z':
            return_string += str[i]
            i += 1
        else:
            uppercase = chr(ord(str[i]) - ascii_offset)
            return_string += uppercase
            i += 1

    return return_string
