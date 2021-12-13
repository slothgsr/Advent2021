import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
file = (r'day1\input.txt')

with open(file) as f:
    lines = [int(line.rstrip('\n')) for line in f]
    previous_line = lines[0]
    higher = 0
    for i in lines[1:]:
        if i > previous_line:
            higher += 1
        previous_line = i

print(higher)