import sys
import math

def upperHalf(values):
    half = (values[1] - values[0]) / 2

    return (values[0] + math.ceil(half), values[1])

def lowerHalf(values):
    half = (values[1] - values[0]) / 2

    return (values[0], values[1] - math.ceil(half))

def decodeSeatId(input):
    rows = (0, 127)
    cols = (0, 7)

    for char in input:
        if char == 'F':
            rows = lowerHalf(rows)
        elif char == 'B':
            rows = upperHalf(rows)
        elif char == 'L':
            cols = lowerHalf(cols)
        elif char == 'R':
            cols = upperHalf(cols)

    return rows[0] * 8 + cols[0]


file = open(sys.argv[1], 'r')
lines = file.readlines()

maxId = 0
minId = -1
present = set()

for line in lines:
    seatId = decodeSeatId(line.strip())

    maxId = seatId if seatId > maxId else maxId
    minId = seatId if minId == -1 or seatId < minId else minId
    present.add(seatId)

print("Max seat ID: {}".format(maxId))

for i in range(minId, maxId):
    if i not in present:
        print("Your seat ID is {}".format(i))

file.close()