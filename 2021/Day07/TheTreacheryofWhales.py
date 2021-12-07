# https://adventofcode.com/2021/day/7
import sys

# Function for calculating used fuel in part one of the puzzle
# Fuel = distance
def simpleFuelFunc(distance, precalc):
    return distance

# Function for calculating used fuel in part two of the puzzle
# Fuel = sum of (1 to distance>
# Precalc = dictionary of pre-calculated results from previous calls
def sumFuelFunc(distance, precalc):
    if distance in precalc:
        return precalc[distance]
    else:
        fuel = sum(range(1, distance + 1))
        precalc[distance] = fuel

        return fuel

# Function for calculating the most optimal position and sum of fuel that is needed
# crabs = list of crab submarines positions
# fuelFunc = function for calculating fuel used for moving to target position
def calculateBest(crabs, fuelFunc):
    minPos = min(crabs)
    maxPos = max(crabs)
    bestPos = -1
    bestFuel = -1
    precalc = {}

    for target in range(minPos, maxPos + 1):
        fuel = 0

        for crabPos in crabs:
            fuel += fuelFunc(abs(target - crabPos), precalc)
        
        if (bestFuel == -1 or fuel < bestFuel):
            bestFuel = fuel
            bestPos = target
    
    return (bestPos, bestFuel)

file = open(sys.argv[1], 'r')
input = file.readlines()

crabs = list(map(lambda x: int(x), input[0].split(',')))

res1 = calculateBest(crabs, simpleFuelFunc)
print(f"Part ONE: best position is {res1[0]} with {res1[1]} fuel used")

res2 = calculateBest(crabs, sumFuelFunc)
print(f"Part TWO: best position is {res2[0]} with {res2[1]} fuel used")

file.close()