file = (r'C:\Users\SlothGSR\Desktop\python_stuff\MyPythonScripts\Advent2021\Day1\input.txt')

with open(file) as f:
    lines = [int(line.rstrip('\n')) for line in f]
    previous_line = lines[0]
    higher = 0
    for i in lines[1:]:
        if i > previous_line:
            higher += 1
        previous_line = i

print(higher)