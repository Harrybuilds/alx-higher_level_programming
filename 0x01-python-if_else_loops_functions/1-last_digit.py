#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = str(number)[-1]

must_print = f"Last digit of {number:d} is {last_digit}"

greater_than_5 = "and is greater than 5"
zero = "and is 0"
less_than_6_not_0 = "and is less than 6 and not 0"

if int(last_digit) > 5:
    print(f"{must_print} {greater_than_5}")

elif int(last_digit) == 0:
    print(f"{must_print} {zero}")
else:
    print(f"{must_print} {less_than_6_not_0}")
