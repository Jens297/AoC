from state import State
from copy import deepcopy

# open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2023\23\input.txt")
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

# create grid to transform it later to a list of states
# for Part B: change all <,>,v,^ to .
def createStates(grid):
    states = []
    for entry in grid:
        symbol = grid[entry]
        if symbol in  ["^", "<", ">", "v"]:
            symbol = '.'
        s = State(entry, symbol)
        states.append(s)
    return states

listofstates = createStates(grid)
#print(listofstates)

def getrightneighbour(p):
    right = (p[0]+1, p[1])
    if right[0] in range(xMax):
        return right
    else:
        return False

def getupperneighbour(p):
    up = (p[0], p[1]-1)
    if up[1] in range(yMax):
        return up
    else:
        return False

def getlowerneighbour(p):
    low = (p[0], p[1]+1)
    if low[1] in range(yMax):
        return low
    else:
        return False

def getleftneighbour(p):
    left = (p[0]-1, p[1])
    if left[0] in range(xMax):
        return left
    else:
        return False
    
def getState(listofstates,point):
    for s in listofstates:
        if s.coords == point:
            return s
    
def getNeighbours(state,listofstates):
    coords = state.coords
    neighbours = []
    l = getleftneighbour(coords)
    r = getrightneighbour(coords)
    u = getupperneighbour(coords)
    d = getlowerneighbour(coords)
    for coord in l,r,u,d:
        # check if in bounds:
        if coord != False:
            newstate = getState(listofstates,coord)
            # make sure to avoid going back
            if newstate.coords != state.cameFrom:
                # neighbours are only valid if . and not #
                if newstate.symbol == ".":
                    # don't visit a field twice
                    if not newstate.visited:
                        newstate.cameFrom = state.coords
                        neighbours.append(newstate)
    return neighbours

def findStartandGoal(listofstates):
    for state in listofstates:
        coords = state.coords
        if (coords[1] == 0) and (state.symbol == "."):
            start = state
        if (coords[1] == yMax-1) and (state.symbol == "."):
            goal = state
    return start, goal

start,goal = findStartandGoal(listofstates)

def goHiking(listofstates):
    start,goal = findStartandGoal(listofstates) 
    to_explore = [start]
    hiking_paths = []

    while to_explore:
        current_state = to_explore.pop(0)
        current_path = current_state.path_to_reach
        current_state.visited = True
        neighbours = getNeighbours(current_state,listofstates)
        # avoid cycles
        for n in neighbours:
            if n in current_path:
                neighbours.remove(n)
            else:
                # save a copy of the current path and add its coordinated
                n.path_to_reach = deepcopy(current_path)
                n.path_to_reach.append(n.coords)
        current_state.visited = False

        # if goal: save path to all paths
        if current_state.coords == goal.coords:
            hiking_paths.append(current_state.path_to_reach)     
        # dfs: update to_explore with nighbours. if no valid neighbours, go back to the last crossroad
        to_explore = neighbours + to_explore
    return hiking_paths


hikingpaths = goHiking(listofstates)
print(len(max(hikingpaths)))
