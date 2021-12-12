# https://adventofcode.com/2021/day/9
import sys

# Parse text input into 2D matrix
def parseMatrix(input):
    matrix = []
    for line in input:
        matrix.append(list(map(lambda x: int(x), line.strip())))

    return matrix

# Initilizes matrix with 0 values in the size of the given matrix
def initBasinMatrix(matrix):
    basin = []
    for i in range(0, len(matrix)):
        basin.append([0] * len(matrix[i]))

    return basin

# Detects is value on given coordinates in the given matrix is low point
def isLowPoint(matrix, i, j):
    # Top
    if i > 0 and matrix[i - 1][j] <= matrix[i][j]:
        return False
    # Left
    if j > 0 and matrix[i][j - 1] <= matrix[i][j]:
        return False
    # Right
    if j < len(matrix[i]) - 1 and matrix[i][j + 1] <= matrix[i][j]:
        return False
    # Bottom
    if i < len(matrix) - 1 and matrix[i + 1][j] <= matrix[i][j]:
        return False

    return True

# Recursively traverses matrix from the low point to the 4 directions and
# sets basin ID in the basin matrix if the point belongs to the same basin
def findBasin(i, j, matrix, basinMatrix, basinId):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) or matrix[i][j] == 9 or basinMatrix[i][j] != 0:
        # If i,j are out of bounds or point has been already marked in basin matrix or point is 9 (height)
        return

    basinMatrix[i][j] = basinId
    findBasin(i - 1, j, matrix, basinMatrix, basinId)
    findBasin(i + 1, j, matrix, basinMatrix, basinId)
    findBasin(i, j - 1, matrix, basinMatrix, basinId)
    findBasin(i, j + 1, matrix, basinMatrix, basinId)

# Counts how many points each basin has and returns sizes of the top 3
def getTop3basinSizes(basinMatrix, maxId):
    sizes = {}
    for i in range(1, maxId):
        sizes[i] = 0
    
    for i in range(0, len(basinMatrix)):
        for j in range(0, len(basinMatrix[i])):
            if basinMatrix[i][j] != 0:
                sizes[basinMatrix[i][j]] += 1
    
    sizes = list(sizes.values())
    sizes.sort(reverse=True)

    return sizes[:3]

# Finds out risk level and top 3 biggest basins
def run(matrix):
    riskLevel = 0
    basinMatrix = initBasinMatrix(matrix)
    basinId = 1

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if isLowPoint(matrix, i, j) is False:
                continue
            riskLevel += matrix[i][j] + 1
            findBasin(i, j, matrix, basinMatrix, basinId)
            basinId += 1
    
    top3 = getTop3basinSizes(basinMatrix, basinId)

    return (riskLevel, top3)



file = open(sys.argv[1], 'r')
input = file.readlines()

matrix = parseMatrix(input)
riskLevel, top3basins = run(matrix)

print(f"I: Risk level of low points is {riskLevel}")
print(f"II: Result of part 2 is {top3basins[0] * top3basins[1] * top3basins[2]}")

file.close