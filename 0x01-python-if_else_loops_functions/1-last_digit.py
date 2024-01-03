#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)
last_digit_str = last_digit[-1]
if int(last_digit_str) > 5:
    print(f"Last digit of {number} is {last_digit_str} and is greater than 5")
elif int(last_digit_str) == 0:
    print(f"Last digit of {number} is {last_digit_str} and is 0")
elif int(last_digit_str) < 6:
    print(f"Last digit of {number} is {last_digit_str} and is less than 6 and not 0")
else:
    pass

