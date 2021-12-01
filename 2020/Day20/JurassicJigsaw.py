import sys
import re
import functools

def parseTiles(lines):
    pattern = re.compile("Tile (\d+):")
    tiles = {}
    id = None
    tile = None

    for line in lines:
        line = line.strip()

        if line == '':
            continue

        match = pattern.match(line)

        if match:
            id = int(match.group(1))
            tile = []
            tiles[id] = tile
        else:
            tile.append(list(line))

    return tiles

def getTopEdge(tile):
    return tile[0]

def getRightEdge(tile):
    edge = []
    lastOffset = len(tile[0]) - 1

    for row in tile:
        edge.append(row[lastOffset])

    return edge

def getBottomEdge(tile):
    return tile[len(tile) - 1]

def getLeftEdge(tile):
    edge = []

    for row in tile:
        edge.append(row[0])

    return edge

# Counts common edges
def commonEdges(tile, other):
    edges = [getTopEdge(tile), getRightEdge(tile), getBottomEdge(tile), getLeftEdge(tile)]
    otherEdges = [getTopEdge(other), getRightEdge(other), getBottomEdge(other), getLeftEdge(other)]
    common = 0

    for edge in edges:
        for otherEdge in otherEdges:
            if edge == otherEdge or edge == list(reversed(otherEdge)):
                common += 1

    return common

# Finds corner tiles
def findCorners(tiles):
    cornerIds = []

    for tileId in tiles:
        commonCount = 0

        for tileOther in tiles:
            if tileId != tileOther:
                commonCount += commonEdges(tiles[tileId], tiles[tileOther])

        if commonCount < 3:
            cornerIds.append(tileId)

    return cornerIds

file = open(sys.argv[1], 'r')
lines = file.readlines()

tiles = parseTiles(lines)
cornerIds = findCorners(tiles)

result = functools.reduce(lambda a,b: a * b, cornerIds)
print(result)

file.close()