import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
file = (r'Day4\sample.txt')

def makeboards(lines):
    boardnum = 0
    boards = []
    count = 0
    for i in lines[1:]:
        if i == '':
            boards.append([])
            boardnum += 1
            count = 0
        else:
            boards[boardnum-1].append(i.split())
        count += 1
    return boards
        

with open(file) as f:
    lines = [line.rstrip('\n') for line in f]


# create a list of strings of the called numbers
called_numbers = lines[0].split(',')

boards = makeboards(lines)
print(boards)
print(called_numbers)



#for num in called_numbers:


# for each called number.  find it in all boards and locate the row and column

# create the boards as matrix/arry?? dictionary possibly?? Use class to label each one?? NumPy???
# create hit boards to match each board 0 for nonhit and 1 for hit???  
# create a checker to check horizontal and vertical. if total value == 5 its a win??
# if win. return remaining board numbers

