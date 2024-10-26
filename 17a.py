from node import node

# open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2023\17\input.txt")
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
            value = int(data[y][x])
            grid.update({key:value})
    
    return grid


grid = createGrid(data)

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
    
def getNeighbours(point):
    neighbours = []
    l = getleftneighbour(point)
    r = getrightneighbour(point)
    u = getupperneighbour(point)
    d = getlowerneighbour(point)
    for coords in l,r,u,d:
        if coords != False:
            n = node(coords, grid[coords])
            n.h = ManhattanDistance(coords,(xMax-1,yMax-1))
            neighbours.append(n)
    return neighbours


def ManhattanDistance(s,g):
    return abs(s[0]-g[0]) + abs(s[1]-g[1])

def getNodewithlowestf(openlist):
    init = openlist[0]
    if len(openlist) == 1:
        return init
    for node in openlist:
        if node.f < init.f:
            init = node
    return init

def reconstruct_path(parent, node):
    path = []
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append((0, 0))  # Add the start node 
    path.reverse()
    return path

def AStar(grid):
    start = node((0,0),0)
    openlist = [start]
    goal = node((xMax-1,yMax-1),grid[(xMax-1,yMax-1)])
    start.f = ManhattanDistance(start.coords, goal.coords)
    start.h = start.f
    start.g = 0
    parent = {}
    closedlist = set()
    max_steps_in_one_direction = 3

    while openlist:
        current_node = getNodewithlowestf(openlist)
        if current_node.coords == goal.coords:
            print("goal reached")
            path = reconstruct_path(parent,current_node.coords)
            return path
            
        openlist.remove(current_node)
        closedlist.add(current_node)
        neighbours = getNeighbours(current_node.coords)
        for neighbour in neighbours:
            if neighbour in closedlist:
                continue
            direction = (neighbour.coords[0] - current_node.coords[0], neighbour.coords[1] - current_node.coords[1])
            if current_node.last_direction == direction:
                steps_in_direction = current_node.steps_in_direction + 1
            else:
                steps_in_direction = 1

            if steps_in_direction > max_steps_in_one_direction:
                continue 
            
            # compute g value
            tentative_g = current_node.g + neighbour.cost
            # check if the neighbour has no g value (not reached yet) or if the
            # new path is better than the current
            if neighbour.g == None or tentative_g < neighbour.g:
                # if new path is better, save the parent
                parent[neighbour.coords] = current_node.coords
                neighbour.g = tentative_g
                neighbour.f = neighbour.h+tentative_g
                neighbour.last_direction = direction
                neighbour.steps_in_direction = steps_in_direction
                # if the neighbour is not in the openlist, add it 
                if neighbour not in openlist:
                    openlist.append(neighbour)


path = AStar(grid)
cost = 0
for element in path:
    cost += grid[element]
# heat loss of entering (0,0) does not count
cost -= grid[path[0]]
print(path)
print(cost)
