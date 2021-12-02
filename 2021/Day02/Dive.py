# https://adventofcode.com/2021/day/2
import sys

file = open(sys.argv[1], 'r')
input = file.readlines()

def partOne(input):
    horizontal = 0
    depth = 0

    for line in input:
        command = line.split(" ")
        value = int(command[1])
        
        if command[0] == 'forward':
            horizontal += value
        elif command[0] == 'down':
            depth += value
        elif command[0] == 'up':
            depth -= value

    print(f"Horizontal {horizontal} x depth {depth} = {horizontal * depth}")

def partTwo(input):
    horizontal = 0
    depth = 0
    aim = 0

    for line in input:
        command = line.split(" ")
        value = int(command[1])
        
        if command[0] == 'forward':
            horizontal += value
            depth += aim * value
        elif command[0] == 'down':
            aim += value
        elif command[0] == 'up':
            aim -= value

    print(f"Horizontal {horizontal} x depth {depth} = {horizontal * depth}")

partOne(input)
partTwo(input)

file.close()