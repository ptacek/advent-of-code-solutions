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

file = open(sys.argv[1], 'r')
lines = file.readlines()

adapters = list(map(lambda x: int(x), lines))
adapters.sort()

print(adapters)

differences = countDifferences(adapters)
print("x = {}\ny = {}\n1x * 3y = {}".format(differences[1], differences[3], differences[1] * differences[3]))


file.close()