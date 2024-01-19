#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    msg = "argument:" if len(sys.argv) - 1 == 1 else "arguments."
    print("{:d} {:s}".format(len(sys.argv) - 1, msg))
    for i in range(len(sys.argv[1:])):
        print("{:d}: {:s}".format(i+1, sys.argv[i+1]))
