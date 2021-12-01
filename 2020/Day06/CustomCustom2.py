import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

groupAnswers = None
total = 0

for line in lines:
    line = line.strip()

    if line == "":
        # Next group
        total += len(groupAnswers)
        groupAnswers = None
        continue

    if groupAnswers is None:
        groupAnswers = set(list(line))
    else:
        groupAnswers = groupAnswers.intersection(set(list(line)))

total += len(groupAnswers)
print("Sum of counts: {}".format(total))

file.close()