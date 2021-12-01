import sys

def readRow(lines, row):
    bags = row.split("contain ")[1]
    totalCount = 1

    if (bags == "no other bags."):
        return totalCount

    for bag in bags.split(", "):
        tmp = bag.split(" ")
        count = int(tmp[0])
        color = " ".join(tmp[1:3])

        totalCount += count * readLines(lines, color)

    return totalCount


def readLines(lines, targetColor):
    for line in lines:
        color = " ".join(line.split(" ")[:2])
        
        if color == targetColor:
            return readRow(lines, line.strip())


file = open(sys.argv[1], 'r')
lines = file.readlines()

count = readLines(lines, "shiny gold") - 1
print(count)

file.close()