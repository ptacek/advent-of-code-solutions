import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

azimuth = 90
east = 0
north = 0

def moveNorth(val):
    global north
    north += val

def moveSouth(val):
    global north
    north -= val

def moveEast(val):
    global east
    east += val

def moveWest(val):
    global east
    east -= val

def moveForward(val):
    global azimuth
    if (azimuth == 90):
        moveEast(val)
    elif (azimuth == 180):
        moveSouth(val)
    elif (azimuth == 270):
        moveWest(val)
    else:
        moveNorth(val)

def turnRight(val):
    global azimuth
    azimuth = (azimuth + val) % 360

def turnLeft(val):
    global azimuth
    azimuth = (azimuth - val) % 360

funcs = {
    'N': moveNorth,
    'S': moveSouth,
    'E': moveEast,
    'W': moveWest,
    'L': turnLeft,
    'R': turnRight,
    'F': moveForward
}

for line in lines:
    action = line[0]
    value = int(line.strip()[1:])

    funcs[action](value)
    
distance = abs(north) + abs(east)
print("Distance: {}".format(distance))
    
file.close()