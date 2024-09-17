# open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2023\16\input.txt")
# read it line by line

lines = input.readlines()
data = []
for line in lines:
    newline = line.strip('\n')
    data.append((newline))

# print(data)
yMax = len(data)
xMax = len(data[0])

def createGrid(data):
    grid = {}
    yMax = len(data)
    xMax = len(data[0])

    for x in range(xMax):
        for y in range(yMax):
            key = (x,y)
            value = data[y][x]
            grid.update({key:value})
    
    return grid

grid = createGrid(data)
#print(grid)

def getrightneighbour(point):
    right = (point[0]+1, point[1])
    if right[0] in range(xMax):
        return right
    else:
        return False

def getupperneighbour(point):
    up = (point[0], point[1]-1)
    if up[1] in range(yMax):
        return up
    else:
        return False

def getlowerneighbour(point):
    low = (point[0], point[1]+1)
    if low[1] in range(yMax):
        return low
    else:
        return False

def getleftneighbour(point):
    left = (point[0]-1, point[1])
    if left[0] in range(xMax):
        return left
    else:
        return False

class Beam:
  def __init__(self, current, direction):
    self.current = current
    self.direction = direction

  def __repr__(self):
    return f"Beam(current={self.current}, direction={self.direction})"
  
  def __eq__(self, other):
    return self.current == other.current and self.direction == other.direction

  def __hash__(self):
    return hash((self.current, self.direction))

startbeam1 = Beam((0,0),'R')
startbeam2 = Beam((-1,0),'R')
startbeam3 = Beam((0,0),'R')

# called with one beam. may return two beams if splintered
def move(listofbeams,grid):
    currentbeam = listofbeams[0]
    dir = currentbeam.direction 
    currentPosition = currentbeam.current
    visited = currentPosition
    processedbeam = listofbeams[0]
 
    if dir == 'R':
        in_grid = getrightneighbour(currentPosition)
        if in_grid == False:
            listofbeams.pop(0)
            return listofbeams,visited, processedbeam
        rightNeighbour = grid[getrightneighbour(currentPosition)]
        currentbeam.current = getrightneighbour(currentPosition)
        if rightNeighbour == '/':
            currentbeam.direction = 'U'
        elif rightNeighbour == '\\':
            currentbeam.direction = 'D'
        elif rightNeighbour == '|':
            currentbeam.direction = 'U'
            splitBeam = Beam(currentbeam.current,'D')
            listofbeams.append(splitBeam)
    elif dir == 'L':
        in_grid = getleftneighbour(currentPosition)
        if in_grid == False:
            listofbeams.pop(0)
            return listofbeams,visited, processedbeam
        leftNeighbour = grid[getleftneighbour(currentPosition)]
        currentbeam.current = getleftneighbour(currentPosition)
        if leftNeighbour == '/':
            currentbeam.direction = 'D'
        elif leftNeighbour == '\\':
            currentbeam.direction = 'U'
        elif leftNeighbour == '|':
            currentbeam.direction = 'U'
            splitBeam = Beam(currentbeam.current,'D')
            listofbeams.append(splitBeam)
    elif dir == 'U':
        in_grid = getupperneighbour(currentPosition)
        if in_grid == False:
            listofbeams.pop(0)
            return listofbeams,visited, processedbeam
        upperNeighbour = grid[getupperneighbour(currentPosition)]
        currentbeam.current = getupperneighbour(currentPosition)
        if upperNeighbour == '/':
            currentbeam.direction = 'R'
        elif upperNeighbour == '\\':
            currentbeam.direction = 'L'
        elif upperNeighbour == '-':
            currentbeam.direction = 'L'
            splitBeam = Beam(currentbeam.current,'R')
            listofbeams.append(splitBeam)
    elif dir == 'D':
        in_grid = getlowerneighbour(currentPosition)
        if in_grid == False:
            listofbeams.pop(0)
            return listofbeams,visited, processedbeam
        lowerNeighbour = grid[getlowerneighbour(currentPosition)]
        currentbeam.current = getlowerneighbour(currentPosition)
        if lowerNeighbour == '/':
            currentbeam.direction = 'L'
        elif lowerNeighbour == '\\':
            currentbeam.direction = 'R'
        elif lowerNeighbour == '-':
            currentbeam.direction = 'L'
            splitBeam = Beam(currentbeam.current,'R')
            listofbeams.append(splitBeam)
    
    return listofbeams, visited, processedbeam

#print(move([startbeam1],grid,[]))

def moveBeams(startBeam,grid):
    visited = []
    beams = []
    alreadyvisitedbeams = set()
    beams.append(startBeam)
    processed = []
    idx =  0
    #while beams:
    while beams:
        movement = move(beams,grid)
        beams = movement[0]
        energized = movement[1]
        visited.append(energized)

        print(beams)
        for beam in beams:
            if beam in processed:
                print("remove", beam)
                beams.remove(beam)
        print(beams)
        idx += 1
    alreadyvisitedbeams.update(visited)
    return 'res', len(alreadyvisitedbeams)

print(moveBeams(startbeam2,grid))

    
#4340,4339,4341
# Solution 1 8389
# Solution 2 8564
