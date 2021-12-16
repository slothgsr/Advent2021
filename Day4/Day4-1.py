import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)

file = (r'Day4\sample.txt')

def makeboards(lines):
    count = 0
    boardnum = 0
    boards = []
    for i in lines[2:]:
        print(list(i.split()))
        if i == '':
             boardnum += 1
        boards[boardnum].add(list(i.split()))
        count += 1
        print("board num " + str(boardnum))
    return boards
        

        
        




with open(file) as f:
    lines = [line.rstrip('\n') for line in f]
called_numbers = lines[0]
print(lines)
print(called_numbers)

print(makeboards(lines))





# create the boards as matrix/arry?? dictionary possibly?? Use class to label each one?? NumPy???
# create hit boards to match each board 0 for nonhit and 1 for hit???  
# create a checker to check horizontal and vertical. if total value == 5 its a win??
# if win. return remaining board numbers

