#https://adventofcode.com/2021/day/10
import sys

# Part two algorithm for calculating score of incomplete line
def calculateIncompleteScore(stack):
    score = 0

    while len(stack) > 0:
        score *= 5
        char = stack.pop()

        if char == '(':
            score += 1
        elif char == '[':
            score += 2
        elif char == '{':
            score += 3
        elif char == '<':
            score += 4

    return score

# Checks line and if it's sytax is corrupted (part one), calculates score of corrupted line
# Otherwise calculates score of incomplete line (part two)
def checkLine(line):
    stack = []
    corruptScore = 0
    incompleteScore = 0
    
    for char in line:
        if char in ['(', '[', '<', '{']:
            stack.append(char)
            continue

        open = stack.pop()
        if char == ')' and open != '(':
            corruptScore = 3
            break
        elif char == ']' and open != '[':
            corruptScore = 57
            break
        elif char == '}' and open != '{':
            corruptScore = 1197
            break
        elif char == '>' and open != '<':
            corruptScore = 25137
            break

    if corruptScore == 0:
        incompleteScore = calculateIncompleteScore(stack)

    return (corruptScore, incompleteScore)

# MAIN
file = open(sys.argv[1], 'r')
input = file.readlines()

score = 0
incompleteScores = []

for line in input:
    corruptScore, incScore = checkLine(line.strip())
    score += corruptScore
    incompleteScores.append(incScore)

# There are zeros for lines that were corrupted and must be filtered out
# Result of part two is middle score after sorting
incompleteScores = list(filter(lambda x: x != 0, incompleteScores))
incompleteScores.sort()
incompleteScore = incompleteScores[int(len(incompleteScores) / 2)]

print(f"I: score of the corrupted lines is {score}")
print(f"II: score of the incomplete lines is {incompleteScore}")

file.close()