#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    counter = len(sys.argv) - 1

    if counter == 0:
        print("{:d} arguments.".format(counter))
    elif counter == 1:
        print("{:d} argument:".format(counter))
        print("{:d}: {}".format(counter, sys.argv[counter]))
    else:
        print("{:d} arguments:".format(counter))
        i = 1
        while i <= counter:
            print("{:d}: {}".format(i, sys.argv[i]))
            i += 1
