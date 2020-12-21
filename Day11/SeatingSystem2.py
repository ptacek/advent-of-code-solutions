import sys

def countOccupied(grid):
    occupied = 0
    for row in grid:
        for col in row:
            if col == '#':
                occupied += 1

    return occupied

def adjacentEmpty(grid, i, j):
    step = 1
    top = True
    topLeft = True
    topRight = True
    bottom = True
    bottomLeft = True
    bottomRight = True
    iOrig = i

    # Rows above
    while i > 0:
        i -= 1
        
        if top and grid[i][j] == '#':
            return False
        elif grid[i][j] == 'L':
            top = False

        if topLeft and j - step >= 0 and grid[i][j - step] == '#':
            return False
        elif j - step >= 0 and grid[i][j - step] == 'L':
            topLeft = False

        if topRight and j + step < len(grid[i]) and grid[i][j + step] == '#':
            return False
        elif j + step < len(grid[i]) and grid[i][j + step] == 'L':
            topRight = False
        
        step += 1

    i = iOrig
    step = 1
    # Rows below
    while i + 1 < len(grid):
        i += 1

        if bottom and grid[i][j] == '#':
            return False
        elif grid[i][j] == 'L':
            bottom = False

        if bottomLeft and j - step >= 0 and grid[i][j - step] == '#':
            return False
        elif j - step >= 0 and grid[i][j - step] == 'L':
            bottomLeft = False

        if bottomRight and j + step < len(grid[i]) and grid[i][j + step] == '#':
            return False
        elif j + step < len(grid[i]) and grid[i][j + step] == 'L':
            bottomRight = False
        
        step += 1

    # Same row
    step = 1
    i = iOrig
    left = True
    right = True

    while j - step >= 0 or j + step < len(grid[i]):
        if left and j - step >= 0 and grid[i][j - step] == '#':
            return False
        if j - step >= 0 and grid[i][j - step] == 'L':
            left = False

        if right and j + step < len(grid[i]) and grid[i][j + step] == '#':
            return False
        if j + step < len(grid[i]) and grid[i][j + step] == 'L':
            right = False

        step += 1

    return True

def adjacentOccupied(grid, i, j):
    occupied = 0

    step = 1
    top = True
    topLeft = True
    topRight = True
    bottom = True
    bottomLeft = True
    bottomRight = True
    iOrig = i

    # Rows above
    while i > 0:
        i -= 1
        
        if top and grid[i][j] == '#':
            occupied += 1
            top = False
        elif grid[i][j] == 'L':
            top = False

        if topLeft and j - step >= 0 and grid[i][j - step] == '#':
            occupied += 1
            topLeft = False
        elif j - step >= 0 and grid[i][j - step] == 'L':
            topLeft = False

        if topRight and j + step < len(grid[i]) and grid[i][j + step] == '#':
            occupied += 1
            topRight = False
        elif j + step < len(grid[i]) and grid[i][j + step] == 'L':
            topRight = False
        
        step += 1

    if occupied >= 5:
        return True

    i = iOrig
    step = 1
    # Rows below
    while i + 1 < len(grid):
        i += 1

        if bottom and grid[i][j] == '#':
            occupied += 1
            bottom = False
        elif grid[i][j] == 'L':
            bottom = False

        if bottomLeft and j - step >= 0 and grid[i][j - step] == '#':
            occupied += 1
            bottomLeft = False
        elif j - step >= 0 and grid[i][j - step] == 'L':
            bottomLeft = False

        if bottomRight and j + step < len(grid[i]) and grid[i][j + step] == '#':
            occupied += 1
            bottomRight = False
        elif j + step < len(grid[i]) and grid[i][j + step] == 'L':
            bottomRight = False
        
        step += 1

    if occupied >= 5:
        return True

    # Same row
    step = 1
    i = iOrig
    left = True
    right = True

    while j - step >= 0 or j + step < len(grid[i]):
        if left and j - step >= 0 and grid[i][j - step] == '#':
            occupied += 1
            left = False
        if j - step >= 0 and grid[i][j - step] == 'L':
            left = False

        if right and j + step < len(grid[i]) and grid[i][j + step] == '#':
            occupied += 1
            right = False
        if j + step < len(grid[i]) and grid[i][j + step] == 'L':
            right = False

        step += 1

    return occupied >= 5

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