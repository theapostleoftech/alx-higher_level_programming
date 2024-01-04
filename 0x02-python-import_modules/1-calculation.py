#!/usr/bin/python3
import calculator_1 as calculate

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calculate.add(a, b)))
    print("{} - {} = {}".format(a, b, calculate.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculate.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculate.div(a, b)))
