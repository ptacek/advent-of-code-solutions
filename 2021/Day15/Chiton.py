#https://adventofcode.com/2021/day/15
import sys

# Note: This solution is based on Dijkstra's algorithm

# I have created separate sets for ranked nodes and not yet ranked nodes
# as an optimization of 'extractBest' function, because of part 2 of the puzzle

# Solution with one set for all not visited nodes is good enough for the first part 

class Node:
    # x,y = coordinates in matrix
    # value = risk level of this one node
    # sum = risk level of path from start to this node
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.sum = None

# Parses text input into matrix of nodes
# Repeat allows to tile the matrix X times with increasing values
# 1 = just the original matrix
# 2+ = tiling 2 or more times 
def parseMatrix(input, repeat):
    matrix = []
    size = len(input)

    for x in range(0, repeat):
        for i, line in enumerate(input):
            row = []
            matrix.append(row)

            for y in range(0, repeat):
                for j, num in enumerate(line.strip()):
                    value = int(num) + x + y
                    xNode = i + x * size
                    yNode = j + y * size
                    row.append(Node(xNode, yNode, value if value <= 9 else value - 9))

    return matrix

# Extracts a node with the best sum of risk levels from the set
# of ranked nodes (removes and returns the node)
def extractBest(nodes):
    best = None

    for node in nodes:
        if node.sum is None:
            continue
        if best is None or node.sum < best.sum:
            best = node

    nodes.remove(best)

    return best

# Ranks path to the node from the previous node
# If node didn't have any rank before, then it must be moved from
# set of nodes to rank to the set of ranked nodes
def rankNode(node, prev, ranked, toRank):
    newVal = prev.sum + node.value

    if node.sum is None:
        node.sum = newVal
        toRank.remove(node)
        ranked.add(node)

    elif newVal < node.sum:
        node.sum = newVal

# Finds the best path from start to all of the nodes
# Ranked = set of nodes that already have some rank (total risk level from start to the node)
# toRank = set of nodes with empty rank
# matrix = 2d array of nodes to keep relation between the nodes and quick access by coordinates
def rank(ranked, toRank, matrix):
    while len(ranked) > 0:
        best = extractBest(ranked)
        
        # Rank all adjacent nodes in 4 directions
        if best.x != len(matrix) - 1:
            bottom = matrix[best.x + 1][best.y]
            rankNode(bottom, best, ranked, toRank)

        if best.x != 0:
            top = matrix[best.x - 1][best.y]
            rankNode(top, best, ranked, toRank)

        if best.y != len(matrix) - 1:
            right = matrix[best.x][best.y + 1]
            rankNode(right, best, ranked, toRank)

        if best.y != 0:
            left = matrix[best.x][best.y - 1]
            rankNode(left, best, ranked, toRank)

# Initialization of parameters for the main algorithm
# and printing result for the destination node
def run(matrix):
    toRank = set()
    ranked = set()

    for row in matrix:
        for node in row:
            toRank.add(node)
    
    matrix[0][0].sum = 0
    toRank.remove(matrix[0][0])
    ranked.add(matrix[0][0])

    rank(ranked, toRank, matrix)
    endRisk = matrix[len(matrix) - 1][len(matrix) - 1].sum

    print(f"Path with lowest risk has risk level {endRisk}")

# MAIN:
file = open(sys.argv[1], 'r')
input = file.readlines()

# Part ONE
matrix = parseMatrix(input, 1)
run(matrix)

# Part TWO
matrix = parseMatrix(input, 5)
run(matrix)

file.close()