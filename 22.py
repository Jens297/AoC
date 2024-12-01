from brick import Brick

#open the file
input = open(r"C:\Users\Jens\Desktop\AoC\2023\22\input.txt")
# read it line by line

# convert an entry from the input list to a brick
def convertEntry(entry,id):
    removetilde = entry.split("~")
    left = removetilde[0].split(',')
    right = removetilde[1].split(',')
    all = left + right
    brick = Brick(id,int(all[0]),int(all[1]),int(all[2]),int(all[3]),int(all[4]),int(all[5]))
    return brick


lines = input.readlines()
listofbricks = []
# convert input to a list of bricks. x is a unique id to identify bricks, starting with 1.
# brick with id = 0 is the floor, see below
x = 1
for line in lines:
    newline = line.strip('\n')
    entry = convertEntry(newline,x)
    listofbricks.append(entry)
    x += 1

# get the max dimensions to create the floor accordingly
xx_max = max(listofbricks, key=lambda brick: brick.xx).xx
yy_max = max(listofbricks, key=lambda brick: brick.yy).yy

# create floor
FLOOR = Brick(0,0,0,0,xx_max,yy_max,0)

# sort the bricklist for the respective key (which adresses an attribute of brick)
def sortbricklist(bricklist,key,reverse):
    if reverse == True:
        return bricklist.sort(reverse=True, key=lambda brick: getattr(brick, key))
    else:
        return bricklist.sort(key=lambda brick: getattr(brick, key))

sortbricklist(listofbricks,'z',False)

# gets a brick and returns a list of cubes (x,y) which are in the brick
# z and zz attributes don't matter in here 
def getlistofhoricontalcubes(brick):
    list = []
    # brick extends on the y axis
    if brick.x == brick.xx:
        start = min(brick.y,brick.yy)
        stop = max(brick.y,brick.yy)
        for r in range(start,stop+1):
            cube = (brick.x,r)
            list.append(cube)
    # brick extends on the x axis        
    else:
        start = min(brick.x,brick.xx)
        stop = max(brick.x,brick.xx)
        for r in range(start,stop+1):
            cube = (r,brick.y)
            list.append(cube)
    return list

# fall gets a brick and updates its z-value
# fallenbricks is a list of bricks which have already fallen to the ground
# the first entry of the list is the brick on the ground
# four different possibilities: horicontal falls on horicontal, horicontal on vertical, vertical on horicontal and vertical on vertical
def fall(brick,fallenbricks):
    # sort with key=zz because the highest zz is the first possibility to hit while falling
    sortbricklist(fallenbricks,'zz',True)
    if brick.horicontal:
        brickcubes = getlistofhoricontalcubes(brick)
        for fallenbrick in fallenbricks:
            if fallenbrick.horicontal:
                fallencubes = getlistofhoricontalcubes(fallenbrick)
                if any(cube in brickcubes for cube in fallencubes):
                    brick.z = fallenbrick.zz+1
                    brick.zz = fallenbrick.zz+1
                    return brick
            else:
                touchpoint = (fallenbrick.xx,fallenbrick.yy)
                if touchpoint in brickcubes:
                    brick.z = fallenbrick.zz+1
                    brick.zz = fallenbrick.zz+1
                    return brick
        return brick 
    # brick vertical
    else:
        touchpoint = (brick.x,brick.y)
        z_offset = brick.zz-brick.z
        for fallenbrick in fallenbricks:
            if fallenbrick.horicontal:
                fallencubes = getlistofhoricontalcubes(fallenbrick)
                if touchpoint in fallencubes:
                    brick.z = fallenbrick.z+1
                    brick.zz = fallenbrick.z+1+z_offset
                    return brick
            else:
                if touchpoint == (fallenbrick.xx,fallenbrick.yy):
                    brick.z = fallenbrick.zz+1
                    brick.zz = fallenbrick.zz+1+z_offset
                    return brick
        return brick 

# let bricks fall to the ground. floor is the very first entry on that list to ensure pieces can hit it and don't fall into the void
fallenbricks = [FLOOR]

for brick in listofbricks:
    fallen = fall(brick,fallenbricks)
    fallenbricks.append(fallen)

# gets two ranges and returns True if there are overlapping values
def ranges_overlap(range1, range2):
    for ele in range1:
        if ele in range2:
            return True
    return False

# gets a list of bricks and a single brick
# returns a new list with bricks that are directly located over the single brick
def getBricksonelevelabove(bricklist,brick):
    list = []
    for b in bricklist:
        if b.z == brick.zz+1:
            list.append(b)
    return list

# gets a bricklist and updates its support attributes
# returns the bricklist with updated attributes
def supports(bricklist):
    #sort with key=z to move from lowest brick up to the top
    sortbricklist(bricklist,'z',False)
    # remove floor to avoid mistakes, it is not needed after all pieces have fallen
    bricklist.pop(0)
    # a brick supports another brick if the z value differs by one
    # and if the x/xx, y/yy values overlap in at least one cube 
    for brick in bricklist:
        # get the bricks directly located above
        bricksabove = getBricksonelevelabove(bricklist,brick)
        for brickabove in bricksabove:
            if ranges_overlap(range(brickabove.x,brickabove.xx+1), range(brick.x,brick.xx+1)) and ranges_overlap(range(brickabove.y,brickabove.yy+1), range(brick.y,brick.yy+1)):
                brick.supports.append(brickabove.tag)
    return bricklist

# update the supported attributes of the fallen bricks
supported = supports(fallenbricks)    

# gets a list of bricks with updated supported attribute
# returns the number of disposable bricks
def PartA(supported):
    result = 0
    sortbricklist(supported,'z',False)
    # for e in supported:
    #     print(e)
    # create a single list with the bricks that are supported by any brick 
    listofsupported = []
    for brick in supported:
        listofsupported.extend(brick.supports)
    # for every brick, starting at the bottom    
    for brick in supported:
        # brick supports no other brick, can be desintegrated
        if len(brick.supports) == 0:
            result +=1
            print("brick", brick.tag, "can be desintegrated")

        else:
            disposable = True
            # if the supported brick is more than one time on the supported list
            # it can be desintegrated as another brick is still supporting it
            
            for supported_brick in brick.supports:
                if listofsupported.count(supported_brick) == 1:
                    disposable = False
            if disposable:
                result += 1
                print("brick", brick.tag, "can be desintegrated")
    return result

print(PartA(supported))
