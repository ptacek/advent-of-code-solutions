#https://adventofcode.com/2021/day/17
import sys

# Parses text input into tuples of coordinates
def parseTargetArea(input):
    input = input.split(": ")[1].split(", ")
    x = input[0].replace("x=", "").split("..")
    y = input[1].replace("y=", "").split("..")

    return ((int(x[0]), int(x[1])), (int(y[0]), int(y[1])))

# Is X,Y inside target area
def inTargetArea(x, y, targetX, targetY):
    return x >= targetX[0] and x <= targetX[1] and y >= targetY[0] and y <= targetY[1]

# Has X,Y already missed target area
def missedTargetArea(x, y, targetX, targetY):
    return x > targetX[1] or y < targetY[0]

# Tries one initial x, y velocity
# Returns True and maximum Y value if hits the target area
# otherwise False and 0
def fire(xVal, yVal, targetX, targetY):
    x = 0
    y = 0
    maxY = 0

    while True:
        x += xVal
        y += yVal

        maxY = y if y > maxY else maxY
        yVal -= 1
        
        if xVal > 0:
            xVal -= 1
        elif xVal < 0:
            xVal += 1

        if missedTargetArea(x, y, targetX, targetY):
            return (False, 0)
        elif inTargetArea(x, y, targetX, targetY):
            return (True, maxY)   

# MAIN:
file = open(sys.argv[1], 'r')
input = file.readlines()[0].strip()

targetX, targetY = parseTargetArea(input)
cnt = 0
totalMaxY = targetY[1]


# Makes sense to fire only forward and not further than end of target area:
for i in range(0, targetX[1] + 1):
    # Makes sense to fire only above target area
    for j in range(targetY[0], -1 * targetY[0]):
        hit, maxY = fire(i, j, targetX, targetY)
        
        if hit is True:
            totalMaxY = maxY if maxY > totalMaxY else totalMaxY 
            cnt += 1

print(f"I: maximum possible Y value is {totalMaxY}")
print(f"II: number of distict possible starting velocities is {cnt}")

file.close()