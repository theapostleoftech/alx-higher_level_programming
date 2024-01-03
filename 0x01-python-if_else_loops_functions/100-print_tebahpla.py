#!/usr/bin/python3
for char in range(ord('z'), ord('A') - 1, -1):
    print("{:c}".format(char)
          if (char - ord('A')) % 2 == 0
          else "{:c}".format(char + 32), end="")

print("")
