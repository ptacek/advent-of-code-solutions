#https://adventofcode.com/2021/day/14
import sys

# NOTE: This version is not good enough for the second part of the puzzle (running 40 steps)

# Creates 2-level dictionary with rules (1st letter, 2nd letter => new letter) 
# and returns it with polymer template (first line of input)
def parseInput(input):
    template = input[0].strip()
    rules = {}

    for line in input[2:]:
        rule = line.strip().split(" -> ")
        
        if rule[0][0] not in rules:
            rules[rule[0][0]] = {}

        rules[rule[0][0]][rule[0][1]] = rule[1]
    
    return (template, rules)

# Algorithm that adds new letters based on given rules in specified number of steps
def buildPolymer(template, rules, steps):
    polymer = []

    for i in range(0, steps):
        polymer = []    

        for j in range(1, len(template)):
            first = template[j - 1]
            second = template[j]
            polymer.append(first)
            polymer.append(rules[first][second])
            
            if j == len(template) - 1:
                polymer.append(second)

        template = polymer
    
    return polymer

# Counts individual letters in the result
def countLetters(polymer):
    counts = {}

    for char in polymer:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    return counts

# MAIN:
file = open(sys.argv[1], 'r')
input = file.readlines()

template, rules = parseInput(input)

polymer = buildPolymer(template, rules, 10)
letters = countLetters(polymer)

sortedCounts = list(letters.values())
sortedCounts.sort()

print(f"I: Most common minus least common = {sortedCounts[-1] - sortedCounts[0]}")

file.close()