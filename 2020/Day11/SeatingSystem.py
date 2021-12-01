import sys

def countOccupied(grid):
    occupied = 0
    for row in grid:
        for col in row:
            if col == '#':
                occupied += 1

    return occupied

def adjacentEmpty(grid, i, j):
    # Row above
    if i >= 1:
        if j >= 1 and grid[i - 1][j - 1] == '#':
            return False
        if grid[i - 1][j] == '#':
            return False
        if j + 1 < len(grid[i]) and grid[i - 1][j + 1] == '#':
            return False
    # Same row - left, right
    if j >= 1 and grid[i][j - 1] == '#':
        return False
    if j + 1 < len(grid[i]) and grid[i][j + 1] == '#':
        return False
    # Row below
    if i + 1 < len(grid):
        if j >= 1 and grid[i + 1][j - 1] == '#':
            return False
        if grid[i + 1][j] == '#':
            return False
        if j + 1 < len(grid[i]) and grid[i + 1][j + 1] == '#':
            return False

    return True

def adjacentOccupied(grid, i, j):
    occupied = 0

    # Row above
    if i >= 1:
        if j >= 1 and grid[i - 1][j - 1] == '#':
            occupied += 1
        if grid[i - 1][j] == '#':
            occupied += 1
        if j + 1 < len(grid[i]) and grid[i - 1][j + 1] == '#':
            occupied += 1
    # Same row - left, right
    if j >= 1 and grid[i][j - 1] == '#':
        occupied += 1
    if j + 1 < len(grid[i]) and grid[i][j + 1] == '#':
        occupied += 1
    # Row below
    if i + 1 < len(grid):
        if j >= 1 and grid[i + 1][j - 1] == '#':
            occupied += 1
        if grid[i + 1][j] == '#':
            occupied += 1
        if j + 1 < len(grid[i]) and grid[i + 1][j + 1] == '#':
            occupied += 1

    return occupied >= 4

def runRules(grid):
    newGrid = []
    changes = 0

    for i in range(0, len(grid)):
        newGrid.append([])

        for j in range(0, len(grid[i])):
            if grid[i][j] == 'L' and adjacentEmpty(grid, i, j):
                newGrid[i].append('#')
                changes += 1
            elif grid[i][j] == '#' and adjacentOccupied(grid, i, j):
                newGrid[i].append('L')
                changes += 1
            else:
                newGrid[i].append(grid[i][j])
    
    return (newGrid, changes)

file = open(sys.argv[1], 'r')
lines = file.readlines()

grid = []

# Parse grid
for line in lines:
    grid.append(list(line.strip()))

# Run rules until the changes stop happening
changes = 1

while changes != 0:
    grid, changes = runRules(grid)

print("There are {} occupied seats".format(countOccupied(grid)))

file.close()