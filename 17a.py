from node2 import Node

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
    
def getNeighbours(node):
    neighbours = []
    coords = (node.x,node.y)
    direction = (node.dx-node.x,node.dy-node.y)
    l = getleftneighbour(coords)
    r = getrightneighbour(coords)
    u = getupperneighbour(coords)
    d = getlowerneighbour(coords)
    # looking right
    if direction == (1,0):
        if u != False:
            up = Node(u[0],u[1],0,1,1)
            neighbours.append(up)
        if d != False:
            down = Node(d[0],d[1],0,-1,1)
            neighbours.append(down)
        if node.steps < 3 and r != False:
            right = Node(r[0],r[1],direction[0],direction[1],node.steps+1)
            neighbours.append(right)
    # left
    elif direction == (-1,0):
        if u != False:
            up = Node(u[0],u[1],0,1,1)
            neighbours.append(up)
        if d != False:
            down = Node(d[0],d[1],0,-1,1)
            neighbours.append(down)
        if node.steps < 3 and l != False:
            left = Node(l[0],l[1],direction[0],direction[1],node.steps+1)
            neighbours.append(left)
    # up
    elif direction == (0,1):
        if l != False:
            left = Node(l[0],l[1],-1,0,1)
            neighbours.append(left)
        if r != False:
            right = Node(r[0],r[1],1,0,1)
            neighbours.append(right)
        if node.steps < 3 and u != False:
            up = Node(u[0],u[1],direction[0],direction[1],node.steps+1)
            neighbours.append(up)
    # down
    elif direction == (0,-1):
        if l != False:
            left = Node(l[0],l[1],-1,0,1)
            neighbours.append(left)
        if r != False:
            right = Node(r[0],r[1],1,0,1)
            neighbours.append(right)
        if node.steps < 3 and d != False:
            down = Node(d[0],d[1],direction[0],direction[1],node.steps+1)
            neighbours.append(down)

    return neighbours

def get_current_node(unvisited):
    return min(unvisited, key=lambda node: node.cost)

infinity = float('inf')

def generate_states(x_range, y_range):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    step_range = range(4) 

    states = []
    for x in range(x_range):
        for y in range(y_range):
            for direction in directions:
                for step in step_range:
                    state = Node(x,y,direction[0],direction[1], step)
                    states.append(state)
    return states

unvisited = generate_states(xMax,yMax)

# sets the cost to reach a state in the list and returns the list with updated cost
def setcost(list,state,cost):
    for element in list:
        if element == state:
            element.cost = cost
    return list

# returns the cost to reach a state in a list of states
def getcost(list,state):
    for element in list:
        if element == state:
            return element.cost

def dijkstra(heatloss, unvisited):
    start1 = Node(0,0,1,0,0)
    goal = (xMax-1,yMax-1)

    #set cost to 0 for start
    for state in unvisited:
        if state == start1:
            state.cost = 0

    while unvisited:
        current_node = get_current_node(unvisited)
        current_node_coords = (current_node.x,current_node.y)
        if current_node_coords == goal:
            return "goal reached",current_node.cost
        else:
            neighbours = getNeighbours(current_node)
            for neighbour in neighbours:
                if neighbour in unvisited:
                    neighbour.coords = (neighbour.x, neighbour.y)
                    tentative_distance = current_node.cost+heatloss[neighbour.coords]
                    currentcost = getcost(unvisited,neighbour)
                    if tentative_distance < currentcost:
                        unvisited = setcost(unvisited,neighbour,tentative_distance)
            unvisited.remove(current_node)


d = dijkstra(grid,unvisited)
print(d)
