#https://adventofcode.com/2021/day/12
import sys

# Class that represents cave and its connection to the other caves
class Cave:
    def __init__(self, name) -> None:
        self.name = name
        self.small = name.islower()
        self.adjacent = []
    
    def connect(self, node):
        self.adjacent.append(node)
        node.adjacent.append(self)

# Parses text input into map (graph) of caves
def createMap(input):
    map = {}

    for line in input:
        names = line.strip().split("-")

        if names[0] not in map:
            map[names[0]] = Cave(names[0])

        if names[1] not in map:
            map[names[1]] = Cave(names[1])
        
        map[names[0]].connect(map[names[1]])
    
    return map

# Function for finding out if cave can be visited (again) - PART ONE
def canVisit(cave, path):
    if cave.small and cave.name in path:
        return False
    return True

# Function for finding out if cave can be visited (again) - PART TWO
def canVisitPartTwo(cave, path):
    if cave.small is not True:
        return True
    if cave.name == 'start':
        return False

    smallVisits = {}

    # TODO optimize
    for caveName in path:
        if caveName.islower() is not True:
            continue

        if caveName not in smallVisits:
            smallVisits[caveName] = 1
        else:
            smallVisits[caveName] += 1

    return cave.name not in smallVisits or len(list(filter(lambda x: x > 1, list(smallVisits.values())))) == 0

# Recurse function for travensing graph of caves
# node = starting node
# path = nodes visited in the past
# checkFunc = function for checking if adjacent node can be visited
def traverse(node, path, checkFunc):
    pathCnt = 0
    path.append(node.name)
    node.visited = True

    if node.name == 'end':
        return 1

    for adj in node.adjacent:
        if checkFunc(adj, path):
            pathCnt += traverse(adj, path.copy(), checkFunc)

    return pathCnt

# MAIN:
file = open(sys.argv[1], 'r')
input = file.readlines()

map = createMap(input)

pathCnt1 = traverse(map['start'], [], canVisit)
print(f"Part one: there are {pathCnt1} paths")

pathCnt2 = traverse(map['start'], [], canVisitPartTwo)
print(f"Part two: there are {pathCnt2} paths")

file.close()