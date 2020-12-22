# https://adventofcode.com/2020/day/2
import sys
import re

# Part one - password policy check
def policyCheckOne(min, max, char, passwd):
    charCount = passwd.count(char)

    return charCount >= first and charCount <= second

# Part two - password policy check
def policyCheckTwo(first, second, char, passwd):
    return (passwd[first - 1] == char) ^ (passwd[second - 1] == char)

input = open(sys.argv[1], 'r')
lines = input.readlines()
validCountPartOne = 0
validCountPartTwo = 0

for line in lines:
    match = re.search('^([0-9]+)-([0-9]+) (.): ([a-z]+)$', line.strip())
    first = int(match.group(1))
    second = int(match.group(2))
    char = match.group(3)
    passwd = match.group(4)

    if policyCheckOne(first, second, char, passwd):
        validCountPartOne += 1

    if policyCheckTwo(first, second, char, passwd):
        validCountPartTwo += 1

print("Part one valid count: {}".format(validCountPartOne))
print("Part two valid count: {}".format(validCountPartTwo))

input.close()