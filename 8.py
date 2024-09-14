import sys

# open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2023\8\input.txt")
# read it line by line
lines = input.readlines()
data = []
for line in lines:
    newline = line.strip('\n')
    data.append((newline))

#creates a list where an entry is a triple (Location, R, L)
tripledata = []
for line in data:
    newline = []
    LOCATION = line[:3]
    LEFT = line[7:10]
    RIGHT = line[12:15] 
    tripledata.append((LOCATION, LEFT, RIGHT))

#creates a dict with key = location, value = [left, right]
def makeDictofData(tripledata):
    dict = {}
    for element in tripledata:
        dict[element[0]] = [element[1], element[2]]
    return dict

mydict = makeDictofData(tripledata)


#create a list of directions
dirs = 'LRLRRRLRRLRRRLRRRLLLLLRRRLRLRRLRLRLRRLRRLRRRLRLRLRRLLRLRRLRRLRRLRRRLLRRRLRRRLRRLRLLLRRLRRRLRLRRLRRRLRRLRLLLRRRLRRLRRLRRRLRRRLRRRLRLRLRLRRRLRRRLLLRRLLRRRLRLRLRRRLRRRLRRLRRRLRLRLLRRRLRLRRLRLRLRRLLLRRRLRRRLRRLRRLRLRRLLRRLRRRLRRRLLRRRLRRLRLLRRLRLRRLLRRRLLLLRRLRRRLRLRRLLRLLRRRLLRRLLRRRLRRRLRRLLRLRLLRRLLRLLLRRRR'
directions = []
for d in dirs:
    directions.append(d)

def iterativeApproach(mydict,directions):
    steps = 0
    LOCATION = 'AAA'
    while LOCATION != 'ZZZ':
        #print(steps)
        steps += 1
        if directions[steps % len(directions)] == 'L':
            LOCATION = mydict[LOCATION][0]
        else:
            LOCATION = mydict[LOCATION][1]   
    return steps

print(iterativeApproach(mydict,directions))

# wrong: 7367
