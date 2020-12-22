import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

east = 0
north = 0
waypointEast = 10
waypointNorth = 1

def moveNorth(val):
    global waypointNorth
    waypointNorth += val

def moveSouth(val):
    global waypointNorth
    waypointNorth -= val

def moveEast(val):
    global waypointEast
    waypointEast += val

def moveWest(val):
    global waypointEast
    waypointEast -= val

def moveForward(val):
    global east
    global north
    global waypointEast
    global waypointNorth
    east += val * waypointEast
    north += val * waypointNorth

def rotateRight(val):
    rotation = val % 360

    if rotation == 90:
        rotateRight90()
    elif rotation == 180:
        rotate180()
    elif rotation == 270:
        rotateLeft90()

def rotateLeft(val):
    rotation = val % 360

    if rotation == 90:
        rotateLeft90()
    elif rotation == 180:
        rotate180()
    elif rotation == 270:
        rotateRight90()

def rotate180():
    global waypointEast
    global waypointNorth
    tmp = waypointEast
    waypointEast = waypointNorth * -1
    waypointNorth = tmp * -1

def rotateLeft90():
    global waypointEast
    global waypointNorth
    tmp = waypointEast
    waypointEast = waypointNorth * -1
    waypointNorth = tmp

def rotateRight90():
    global waypointEast
    global waypointNorth
    tmp = waypointEast
    waypointEast = waypointNorth
    waypointNorth = tmp * -1

funcs = {
    'N': moveNorth,
    'S': moveSouth,
    'E': moveEast,
    'W': moveWest,
    'L': rotateLeft,
    'R': rotateRight,
    'F': moveForward
}

for line in lines:
    action = line[0]
    value = int(line.strip()[1:])

    funcs[action](value)
    print("{}, WE: {}, WN: {}, SE: {}, SN: {}".format(line.strip(), waypointEast, waypointNorth, east, north))
    
distance = abs(north) + abs(east)
print("Distance: {}".format(distance))
    
file.close()