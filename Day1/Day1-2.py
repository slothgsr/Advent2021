file = (r'C:\Users\SlothGSR\Desktop\python_stuff\MyPythonScripts\Advent2021\Day1\input.txt')

with open(file) as f:
    lines = [int(line.rstrip('\n')) for line in f]
    previous_set = sum(lines[0:3])
    higher = 0
    for i in range(len(lines)):
        if sum(lines[i:i+3]) > previous_set:
            higher += 1
        previous_set = sum(lines[i:i+3])

print(higher)