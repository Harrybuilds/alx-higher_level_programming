#!/usr/bin/python3

def uppercase(str):
    return_string = ''
    i = 0
    ascii_offset = ord('a') - ord('A')

    while i != len(str):
        if str[i] < 'a' or str[i] > 'z':
            new = str[i]
        else:
            new = chr(ord(str[i]) - ascii_offset)
        print("{}".format(new), end='')
        i += 1
    print()
