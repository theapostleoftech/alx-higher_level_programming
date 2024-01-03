#!/usr/bin/python3
for digit in range(10):
    for _digit in range(digit + 1, 10):
        print("{:d}{}".format(digit, _digit), end=",")
