#https://adventofcode.com/2021/day/11
import sys

# Class that represents octopus. It's energy and wheter has it flashed in current round
class Octopus:
    def __init__(self, energy) -> None:
        self.energy = energy
        self.flash = False

    def __repr__(self):
        return str(self.energy)

# Parses text into matrix of octopuses
def parseInput(input):
    matrix = []

    for line in input:
        row = []
        matrix.append(row)

        for energy in line.strip():
            row.append(Octopus(int(energy)))            

    return matrix

# Increases energy of and octopus on coordinates i,j in the matrix 
# and performs another steps if needed
def increaseEnergy(i, j, matrix):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]):
        # out of bounds
        return 0
    
    octopus = matrix[i][j]

    if octopus.flash is True:
        # Octopus already flashed in this round
        return 0
    elif octopus.energy < 9:
        octopus.energy += 1
        return 0

    # Octopus will now flash and will increase all adjacent positions (if possible)
    octopus.energy = 0
    octopus.flash = True
    flashCount = 1

    flashCount += increaseEnergy(i - 1, j, matrix)
    flashCount += increaseEnergy(i - 1, j + 1, matrix)
    flashCount += increaseEnergy(i , j + 1, matrix)
    flashCount += increaseEnergy(i + 1, j + 1, matrix)
    flashCount += increaseEnergy(i + 1, j, matrix)
    flashCount += increaseEnergy(i + 1, j - 1, matrix)
    flashCount += increaseEnergy(i, j - 1, matrix)
    flashCount += increaseEnergy(i - 1, j - 1, matrix)

    return flashCount

# Resets flash flag for all octopuses
def resetFlash(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j].flash = False

# Runs one step (round)
def runStep(matrix):
    flashCount = 0
    resetFlash(matrix)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            flashCount += increaseEnergy(i, j, matrix)

    return flashCount

# Runs as many steps is needed to find out the result of the part 2 of the puzzle and prints results
def run(matrix):
    totalFlashCount = 0
    step = 0

    while True:
        step += 1
        fleshCount = runStep(matrix)
        totalFlashCount += fleshCount

        if step == 100:
            print(f"I: There have benn {totalFlashCount} flashes after {step} steps")
        if fleshCount == 100:
            print(f"II: All octopuses flashed in step {step}")
            break

# MAIN:
file = open(sys.argv[1], 'r')
input = file.readlines()

matrix = parseInput(input)
run(matrix)

file.close()