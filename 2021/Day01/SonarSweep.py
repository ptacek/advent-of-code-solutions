# https://adventofcode.com/2021/day/1
import sys

file = open(sys.argv[1], 'r')
input = list(map(lambda line: int(line), file.readlines()))

def countIncreases(input):
    prev = None
    increaseCount = 0

    for depth in input:
        if prev is not None and depth > prev:
            increaseCount += 1

        prev = depth

    return increaseCount

def sumWindows(input):
    windows = []
    i = 0

    for i, depth in enumerate(input):
        windows.append(depth)

        if i > 0:
            windows[i - 1] += depth
        if i > 1:
            windows[i - 2] += depth
    
    return windows

count = countIncreases(input)
print(f"The depth has increased {count} times")
count = countIncreases(sumWindows(input))
print(f"The depth has increased {count} times with 3-measurements sliding window")

file.close()