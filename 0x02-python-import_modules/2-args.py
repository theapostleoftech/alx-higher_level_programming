#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    plural_s = 's' if argc != 1 else ''

    print("{} argument{}".format(argc, plural_s) + ("." if argc == 0 else ":"))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
