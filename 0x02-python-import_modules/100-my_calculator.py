#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    if len(sys.argv[1:]) != 3:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)

    operations = ["+", "-", "*", "/"]
    
    if sys.argv[2] in operations:

        operation = operations.index(sys.argv[2])

        if operation == 0:
            print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {cal.add(int(sys.argv[1]), int(sys.argv[3]))}")
        elif operation == 1:
             print("{} {} {} = {}".format(sys.argv[1],sys.argv[2],sys.argv[3],cal.sub(int(sys.argv[1]), int(sys.argv[3]))))
        elif operation == 2:
             print("{} {} {} = {}".format(sys.argv[1],sys.argv[2],sys.argv[3],cal.mul(int(sys.argv[1]), int(sys.argv[3]))))
        else:
             print("{} {} {} = {}".format(sys.argv[1],sys.argv[2],sys.argv[3],cal.div(int(sys.argv[1]), int(sys.argv[3]))))
    else:
        print("{}".format("Unknown operator. Available operators: +, -, * and / "))
        sys.exit(1)
