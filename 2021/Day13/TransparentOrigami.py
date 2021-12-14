#https://adventofcode.com/2021/day/13
import sys

# Creates matrix based on min/max dot coordinates and puts dots on that cordinates (visible dot = #)
def createMatrix(coords):
    xMax = -1
    yMax = -1

    for coord in coords:
        if coord[1] > xMax:
            xMax = coord[1]
        if coord[0] > yMax:
            yMax = coord[0]

    matrix = []

    for i in range(0, xMax + 1):
        matrix.append([' '] * (yMax +1))

    for coord in coords:
        matrix[coord[1]][coord[0]] = '#'

    return matrix

# Parses text lines into list of coordinates and list of folding instructions (separated by empty line)
# Returns matrix initialized from the coordinates and list of instructions
def parseInput(input):
    coords = []
    folds = []
    
    for line in input:
        line = line.strip()
        
        if line == "":
            continue
        elif line.startswith("fold"):
            folds.append(line.split(" ")[-1].split("="))
        else:
            coords.append(tuple(map(lambda x: int(x), line.split(","))))

    return (createMatrix(coords), folds)

# Copies the upper half of the original matrix to the new matrix and mirrors the lower half
# Note: x and y are switched in the puzzle, so y is the number of folding row
def foldHorizontal(matrix, y):
    newMatrix = []

    for i in range(0, y):
        newMatrix.append(matrix[i])

    for i in range(y + 1, len(matrix)):
        mirrorRow = 2 * y - i

        for j in range(0, len(matrix[i])):
            if matrix[i][j] == '#':
                newMatrix[mirrorRow][j] = '#'

    return newMatrix
    
# Copies the left half of the original matrix to the new matrix and mirrors the right half
# Note: x and y are switched in the puzzle, so x is the number of folding column
def foldVertical(matrix, x):
    newMatrix = []
    
    for i in range(0, len(matrix)):
        row = []
        newMatrix.append(row)

        for j in range(0, len(matrix[i])):
            if j < x:
                row.append(matrix[i][j])
            elif j > x and matrix[i][j] == '#':
                mirrorCol = 2 * x - j
                newMatrix[i][mirrorCol] = '#'

    return newMatrix

# Counts visible dots (#) in the matrix (Result of the part one) 
def countVisible(matrix):
    count = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == '#':
                count += 1
    
    return count

# Prints resulting matrix after folding, which should represent 8 characters
def printResult(matrix):
    print("II:")
    for row in matrix:
        print(row)

# Runs folding algorithms until there are folding instructions and prints results
def run(matrix, folds):
    for i, fold in enumerate(folds):
        if fold[0] == 'y':
            matrix = foldHorizontal(matrix, int(fold[1]))
        else:
            matrix = foldVertical(matrix, int(fold[1]))
        
        if i == 0:
            visibleCount = countVisible(matrix)
            print(f"I: There were {visibleCount} visible dots after first fold")
    
    printResult(matrix)

# MAIN:
file = open(sys.argv[1], 'r')
input = file.readlines()

matrix, folds = parseInput(input)
run(matrix, folds)

file.close()