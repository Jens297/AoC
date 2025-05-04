import heapq
# open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2024\16\input.txt")
lines = input.readlines()
data = []
for line in lines:
    newline = line.strip('\n')
    data.append((newline))

yMax = len(data)
xMax = len(data[0])

def createGrid(data):
    grid = {}
    for x in range(xMax):
        for y in range(yMax):
            key = (x,y)
            value = data[y][x]
            grid.update({key:value})
    return grid

grid = createGrid(data)

# gets a coordinate (x,y)
# returns True if it is in bounds of the grid and no wall, else False
def inBounds(coordinate):
    if grid[coordinate] != "#":
        if (coordinate[0] < xMax) and (coordinate[0] > -1):
            if (coordinate[1] < yMax) and (coordinate[1] > -1):
                return True
    return False

# get coordinates of the start and end tile
def getStartAndEnd(grid):
    for key,value in grid.items():
        if value == "S":
            start = key
        elif value == "E":
            end = key
    return start,end

start,end = getStartAndEnd(grid)

# gets a position and direction and returns a list of reachable neighbours
# an element of the list goes like (coords,weight,direction)
def getNeighbours(position,direction):
    u = (position[0],position[1]-1)
    d = (position[0],position[1]+1)
    l = (position[0]-1,position[1])
    r = (position[0]+1,position[1])
    neighbours = []
    if direction == "^":
        candidates = [(u,1,"^"),(d,2001,"v"),(l,1001,"<"),(r,1001,">")]
    elif direction == "v":
        candidates = [(d,1,"v"),(u,2001,"^"),(l,1001,"<"),(r,1001,">")]
    elif direction == ">":
        candidates = [(r,1,">"),(l,2001,"<"),(d,1001,"v"),(u,1001,"^")]
    elif direction == "<":
        candidates = [(l,1,"<"),(r,2001,">"),(d,1001,"v"),(u,1001,"^")]
    for candidate in candidates:
        if inBounds(candidate[0]):
            neighbours.append(candidate)
    return neighbours

# initialize a grid with key = coordinate,direction and value = distance from start
def initializeDistances(grid):
    distances = {}
    directions = ["^","v","<",">"]
    for key in grid.keys():
        for direction in directions:
            distances[key,direction] = float('inf')
    return distances


def dijkstra(start):
    # initialize distances as a grid
    distances = initializeDistances(grid)
    # set distance for start tile
    distances[start,"<"] = 0

    # Min-Heap: (node,distance,direction)
    heap = [(start,0,"<")]
    while heap:
        current_node = heapq.heappop(heap)
        current_position = current_node[0]
        current_distance = current_node[1]
        current_direction = current_node[2]
        # if cheaper distance already found --> skip
        if current_distance > distances[current_position,current_direction]:
            continue
        neighbours = getNeighbours(current_position,current_direction)
        for neighbour in neighbours:
            weight = neighbour[1]
            direction = neighbour[2]
            distance = current_distance+weight
            if distance < distances[neighbour[0],direction]:
                distances[neighbour[0],direction] = distance
                heapq.heappush(heap, (neighbour[0],distance,direction))
    return distances[end,"<"],distances[end,">"],distances[end,"v"],distances[end,"^"]

print(dijkstra(start))
