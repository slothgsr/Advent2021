file = (r'C:\Users\SlothGSR\Desktop\python_stuff\MyPythonScripts\Advent2021\Day2\input.txt')

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

forward = 0
depth = 0

for i in lines:
    if "forward" in i:
        forward += int(i[8])
    if "down" in i:
        depth += int(i[5])
    if "up" in i:
        depth -= int(i[3])

print(forward * depth)
