import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)

file = (r'Day3\input.txt')

digit0 = []
digit1 = []
digit2 = []
digit3 = []
digit4 = []
digit5 = []
digit6 = []
digit7 = []
digit8 = []
digit9 = []
digit10 = []
digit11 = []


def findmax(x):
    zeros = x.count("0")
    ones = x.count("1")
    if zeros > ones:
        return 0
    else:
        return 1

def findmin(x):
    zeros = x.count("0")
    ones = x.count("1")
    if zeros < ones:
        return 0
    else:
        return 1



with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

    for line in lines:
        for i in range(len(line)):
        # str(digit) + str(i).append(line[i])
            digit0.append(line[0])
            digit1.append(line[1])
            digit2.append(line[2])
            digit3.append(line[3])
            digit4.append(line[4])
            digit5.append(line[5])
            digit6.append(line[6])
            digit7.append(line[7])
            digit8.append(line[8])
            digit9.append(line[9])
            digit10.append(line[10])
            digit11.append(line[11])

maxnum = ''      
maxnum += str(findmax(digit0))
maxnum += str(findmax(digit1))
maxnum += str(findmax(digit2))
maxnum += str(findmax(digit3))
maxnum += str(findmax(digit4))
maxnum += str(findmax(digit5))
maxnum += str(findmax(digit6))
maxnum += str(findmax(digit7))
maxnum += str(findmax(digit8))
maxnum += str(findmax(digit9))
maxnum += str(findmax(digit10))
maxnum += str(findmax(digit11))


minnum =''
minnum += str(findmin(digit0))
minnum += str(findmin(digit1))
minnum += str(findmin(digit2))
minnum += str(findmin(digit3))
minnum += str(findmin(digit4))
minnum += str(findmin(digit5))
minnum += str(findmin(digit6))
minnum += str(findmin(digit7))
minnum += str(findmin(digit8))
minnum += str(findmin(digit9))
minnum += str(findmin(digit10))
minnum += str(findmin(digit11))


print(int(maxnum, 2) * int(minnum, 2))