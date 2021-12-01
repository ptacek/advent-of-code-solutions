import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

groupAnswers = set()
total = 0

for line in lines:
    line = line.strip()

    if line == "":
        # Next group
        total += len(groupAnswers)
        groupAnswers = set()
        continue

    groupAnswers = groupAnswers.union(set(list(line)))

total += len(groupAnswers)
print("Sum of unique counts: {}".format(total))

file.close()