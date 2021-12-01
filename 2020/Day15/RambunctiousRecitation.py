import sys

file = open(sys.argv[1], 'r')
line = file.readlines()[0]
numbers = list(map(lambda x: int(x), line.split(",")))

turn = 1
spoken = {}

# Part one: 2020, part two: 30000000
targetTurns = 30000000

for num in numbers[:-1]:
    spoken[num] = turn
    turn += 1

num = numbers[-1:][0]

while turn != targetTurns:
    if num not in spoken:
        spoken[num] = turn
        num = 0
    else:
        nextNum = turn - spoken[num]
        spoken[num] = turn
        num = nextNum

    turn += 1
    
print("The {}th number is {}".format(targetTurns, num))

file.close()