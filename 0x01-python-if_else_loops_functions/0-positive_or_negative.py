#!/usr/bin/python3
import random
number = random.randint(-10, 10)

positive = "is positive"
negative = "is negative"
zero = "is zero"


if number < 0:
    print(f"{number} {negative}")
elif number == 0:
    print(f"{number} {zero}")
else:
    print(f"{number} {positive}")
