#!/usr/bin/python3
print("".join([chr(i)
               if i % 2 == 0
               else chr(i).lower()
               for i in range(ord('Z'), ord('A') - 1, -1)]))
