#!/usr/bin/env python3
#Author = Siddhartha Shrestha
#Student id = 160706222

import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)

name = sys.argv[1]
age = int(sys.argv[2])

print('Hi ' + name + ', you are ' + str(age) + ' years old.')