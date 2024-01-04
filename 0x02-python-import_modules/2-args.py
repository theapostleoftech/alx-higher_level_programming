#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argv_len = len(argv) - 1

    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
    else:
        print(f"{argv_len} arguments:")

    for i, arg in enumerate(argv[1:], start=1):
        print(f"{i}: {arg}")
