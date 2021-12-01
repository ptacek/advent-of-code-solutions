import sys
import math

file = open(sys.argv[1], 'r')
lines = file.readlines()

time = int(lines[0])
ids = list(filter(lambda x: x != 'x', lines[1].strip().split(',')))

bestResult = None

for shuttleId in ids:
    shuttleId = int(shuttleId)
    waiting = math.ceil(time / shuttleId) * shuttleId - time
    
    if bestResult is None or bestResult['waiting'] > waiting:
        bestResult = {"shuttle": shuttleId, "waiting": waiting}

print(bestResult)
print(bestResult['waiting'] * bestResult['shuttle'])

file.close()