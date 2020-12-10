# https://adventofcode.com/2020/day/3
import sys

lines = open(sys.argv[1], 'r').readlines()
grid = []

for line in lines:
    grid.append(list(line.strip()))

def countTreesInSlope(grid, right, down):
    patternHeight = len(grid)
    patternWidth = len(grid[0])
    posX = 0
    posY = 0
    trees = 0

    while posY < patternHeight - 1:
        posX = (posX + right) % patternWidth
        posY += down
        
        if grid[posY][posX] == '#':
            trees += 1
    
    return trees

combinations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1

for comb in combinations:
    trees = countTreesInSlope(grid, comb[0], comb[1])
    product *= trees
    print("Number of trees ({}, {}): {}".format(comb[0], comb[1], trees))

print("Product of results: {}".format(product))
