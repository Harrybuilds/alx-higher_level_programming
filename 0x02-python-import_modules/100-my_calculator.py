#!/usr/bin/python3

if __name__ == '__main__':
    import calculator_1 as cal
    import sys as s

    len_argv = len(s.argv)

    if len_argv != 4:
        print("{} {} <a> <operator> <b>".format("Usage:", s.argv[0]))
        exit(1)

    num1, num2 = int(s.argv[1]), int(s.argv[3])

    if s.argv[2] == '+':
        result = cal.add(num1, num2)
        print("{} {} {} = {}".format(num1, s.argv[2], num2, result))

    elif s.argv[2] == '-':
        result = cal.sub(num1, num2)
        print("{} {} {} = {}".format(num1, s.argv[2], num2, result))

    elif s.argv[2] == '*':
        result = cal.mul(num1, num2)
        print("{} {} {} = {}".format(num1, s.argv[2], num2, result))

    elif s.argv[2] == '/':
        result = cal.div(num1, num2)
        print("{} {} {} = {}".format(num1, s.argv[2], num2, result))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
