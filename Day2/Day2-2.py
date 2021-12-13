import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)

file = (r'day2\input.txt')

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

forward = 0
depth = 0
aim = 0

for i in lines:
    if "forward" in i:
        forward += int(i[8])
        depth += aim * int(i[8])
    if "down" in i:
        aim += int(i[5])
    if "up" in i:
        aim -= int(i[3])

print(forward * depth)
