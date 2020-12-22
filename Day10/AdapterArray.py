import sys

# Part ONE
def countDifferences(adapters):
    differences = {}
    prev = 0

    for joltage in adapters:
        diff = joltage - prev
        prev = joltage

        differences[diff] = differences.get(diff, 0) + 1

    # Output device - always 3 jolts difference
    differences[3] += 1

    return differences

# Part TWO
def countArrangements(adapters, i, ways):
    joltage = adapters[i]

    if i + 1 < len(adapters):
        ways = countArrangements(adapters, i + 1, ways)
    
    if i + 2 < len(adapters) and adapters[i + 2] - joltage <= 3:
        ways += 1
        ways = countArrangements(adapters, i + 2, ways)
    
    if i + 3 < len(adapters) and adapters[i + 3] - joltage <= 3:
        ways += 1
        ways = countArrangements(adapters, i + 3, ways)

    return ways

file = open(sys.argv[1], 'r')
lines = file.readlines()

adapters = [0] + list(map(lambda x: int(x), lines))
adapters.sort()

print(adapters)

differences = countDifferences(adapters)
print("x = {}\ny = {}\n1x * 3y = {}".format(differences[1], differences[3], differences[1] * differences[3]))
print(countArrangements(adapters, 0, 1))

file.close()