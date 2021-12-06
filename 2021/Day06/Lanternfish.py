# https://adventofcode.com/2021/day/6

# Note: naive approach with adding new timers (fish) to the array would not work efficiently enough
# for the second part of the puzzle
import sys

file = open(sys.argv[1], 'r')
input = file.readlines()

# Adds number of fish under timer key or sets intial value if key is not yet present
def addOrInit(generation, timer, fishCount):
    if timer not in generation:
        generation[timer] = fishCount
    else:
        generation[timer] += fishCount

# Sets fish numbers from previous generation to next generation
def nextGeneration(generation):
    next = {}

    for timer in generation:
        if timer == 0:
            addOrInit(next, 6, generation[timer])
            addOrInit(next, 8, generation[timer])
        else:
            addOrInit(next, timer -1, generation[timer])

    return next

# Initializes first generation of fish timers based on text input
def initGeneration(input):
    generation = map(lambda x: int(x), input[0].split(','))
    timers = {}

    for timer in generation:
        if timer in timers:
            timers[timer] += 1
        else:
            timers[timer] = 1
    
    return timers

# MAIN - iterates fish generations until the 80 (puzzle part one) and 256 days (puzzle part two) 
generation = initGeneration(input)

for i in range(0, 256):
    if i == 80:
        fish = sum(generation.values())
        print(f"There are {fish} fish after {i} days (PART ONE)")
    
    generation = nextGeneration(generation)

fish = sum(generation.values())
print(f"There are {fish} fish after 256 days (PART TWO)")

file.close()