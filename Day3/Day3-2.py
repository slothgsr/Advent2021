import os
import sys


def breakdown(x,y):
    codes = []
    for i in range(len(x[0])):
        codes.append(list())
    for i in x:
        position = 0
        for number in i:
            codes[position].append(number)
            position += 1
    position = 0
    newcode = []
    for i in range(len(codes)):
        zeros = codes[position].count('0')
        ones = codes[position].count('1')
        if zeros == ones:
            if y == min:
                newcode.append("0")
            else:
                newcode.append("1")
        if zeros > ones:
            if y == min:
                newcode.append("1")
            else:
                newcode.append("0")
        else:
            if y == min:
                newcode.append("0")
            else: 
                newcode.append("1")
        position += 1
    result =""
    for i in newcode:
        result += i
    return result

def rbreakdown(lines,minmax):
    codes = lines[:]
    position = 0
    while len(codes) > 1:
        newcode =[]
        digit = (breakdown(codes,minmax)[position])
        for x in codes:
            if x[position]== str(digit):
                newcode.append(x)
        position += 1
        codes = newcode[:]
    return(int(codes[0],2))

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)

file = (r'Day3\input.txt')

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

    minnum =(breakdown(lines, min))  
    maxnum =(breakdown(lines, max)) 
    print("Gammarate * Epsilon rate = " + str(int(maxnum, 2) * int(minnum, 2)))


    corate = rbreakdown(lines,min)
    oxyrate = rbreakdown(lines,max)

    print(corate * oxyrate)