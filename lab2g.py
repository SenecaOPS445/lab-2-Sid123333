#!/usr/bin/env python3
#Author = Siddhartha Shrestha
#Student id = 160706222
import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")