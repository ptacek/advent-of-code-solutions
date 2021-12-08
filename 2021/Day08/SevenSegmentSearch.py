# https://adventofcode.com/2021/day/8
import sys

# Decodes which combination of segments corresponds to which number
# Note: This is probably too compliacted. I just looked at the numbers and wrote down how would i deduce them and it works
def decodeNumbersMapping(line):
    mapping = {}
    # Parse signals into sets and sort them by length for easy access by number of segments
    sets = list(map(lambda x: set(x), line.split(" ")))
    sets.sort(key = lambda x: len(x))

    # Signals with only one possible mapping
    mapping[1] = sets[0]
    mapping[4] = sets[2]
    mapping[7] = sets[1]
    mapping[8] = sets[9]

    # Number 6 is 6-segments signal that also has common segments with both segments of number 1
    # This leaves only two possible 6-segment signals to be number 0 or 9
    if sets[0].intersection(sets[6]) != sets[0]:
        mapping[6] = sets[6]
        possible09 = [sets[7], sets[8]]
    elif sets[0].intersection(sets[7]) != sets[0]:
        mapping[6] = sets[7]
        possible09 = [sets[6], sets[8]]
    elif sets[0].intersection(sets[8]) != sets[0]:
        mapping[6] = sets[8]
        possible09 = [sets[6], sets[7]]

    # Number 3 is 5-segments signal that also has common segments with both segments of number 1
    # This leaves only two possible 5-segment signals to be number 2 or 5
    if sets[0].intersection(sets[3]) == sets[0]:
        mapping[3] = sets[3]
        possible25 = [sets[4], sets[5]]
    elif sets[0].intersection(sets[4]) == sets[0]:
        mapping[3] = sets[4]
        possible25 = [sets[3], sets[5]]
    elif sets[0].intersection(sets[5]) == sets[0]:
        mapping[3] = sets[5]
        possible25 = [sets[3], sets[4]]

    # Segments 'b' and 'e' are the only common segments of number 6 and 3
    be = mapping[6] - mapping[3]

    # Number 0 is signal that has both 'b' and 'e' segments. The other 6-segment one is number 9
    if be.intersection(possible09[0]) == be:
        mapping[0] = possible09[0]
        mapping[9] = possible09[1]
    else:
        mapping[0] = possible09[1]
        mapping[9] = possible09[0]

    # Number 2 is signal that has 2 segments in common with number 4. The other 5-segment one is 5
    if len(possible25[0].intersection(mapping[4])) == 2:
        mapping[2] = possible25[0]
        mapping[5] = possible25[1]
    else:
        mapping[2] = possible25[1]
        mapping[5] = possible25[0]

    return mapping

# Puzzle PART ONE
# Count how many numbers 1, 4, 7 or 8 are in the line (the ones that are recognizable just by number of segments)
def countEasyNumbers(segments):
    return len(list(filter(lambda num: len(num) in [2, 3, 4, 7], segments)))

# Decode signal of one digit, base on mapping between numbers and signals
def decodeDigit(digit, mapping):
    for number, segments in mapping.items():
        if digit == segments:
            return str(number)
    
# Decode number on one line by decoding its individual digits and concatenating them
def decodeNumber(segments, mapping):
    numStr = "".join(map(lambda digit: decodeDigit(digit, mapping), segments))
    
    return int(numStr)

# MAIN
file = open(sys.argv[1], 'r')
input = file.readlines()
countEasy = 0
sumTotal = 0

for line in input:
    line = line.strip().split(" | ")
    mapping = decodeNumbersMapping(line[0])
    segments = list(map(lambda x: set(x), line[1].split(" ")))
    
    countEasy += countEasyNumbers(segments)
    sumTotal += decodeNumber(segments, mapping)

print(f"I: Number of easily decoded digits is {countEasy}")
print(f"II: Sum of all decoded numbers is {sumTotal}")

file.close()