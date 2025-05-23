# open file
with open(r"C:\Users\Jens\Desktop\AoC\2024\9\input.txt", 'r', encoding='utf-8') as file:
    diskmap = file.read()

def iseven(num):
    return num % 2 == 0

# transforms the diskmap to a list to represent files and spaces
# returns this list and the number of dots aka spaces to know how much file blocks must be moved
def transformDiskmap(diskmap):
    transformed = []
    number_of_dots = 0
    idx = 0
    for x in range(len(diskmap)):
        if iseven(x):
            transformed.extend(int(diskmap[x])*str(idx))
            idx += 1
        else:
            transformed.extend((int(diskmap[x])*'.'))
            number_of_dots += int(diskmap[x])
    return transformed,number_of_dots

print(transformDiskmap(diskmap))

# gets a transformed diskmap and returns a list with no spaces between blocks
def no_dots(list):
    new_list = []
    for ele in list:
        if ele != ".":
            new_list.append(ele)
    return new_list

# move all the blocks 
def move(diskmap):
    diskmap,number_of_dots = transformDiskmap(diskmap)
    # get a list of the blocks which need to be moved
    to_move = diskmap[len(diskmap)-number_of_dots:]
    # eliminate spaces from this list to get only the blocks
    to_move = no_dots(to_move)
    # reverse it to fill up the spaces properly from the last to the first
    to_move.reverse() 
    x = 0
    for block in to_move:
        print("move element",x)
        # get the index of the first free space in the diskmap
        first_dot = diskmap.index(".")
        # insert block
        diskmap[first_dot] = block
        x+=1
        # return only the blocks, trailing spaces not needed for calculating checksum
    return diskmap[:len(diskmap)-number_of_dots]
    
def solveA(diskmap):
    diskmap = move(diskmap)
    res = 0
    for x in range(len(diskmap)):
        res += x*int(diskmap[x])
    return res


print(solveA(diskmap))
