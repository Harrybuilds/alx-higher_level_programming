#!/usr/bin/python3
if __name__ == "__main__":
    import add_0 as ad

    def new_add(a, b):
        return a - b

    add = ad.add

    a = 1
    b = 2

    if a == 1 and b == 2:
        add = new_add
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
