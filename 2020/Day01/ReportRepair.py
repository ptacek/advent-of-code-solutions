# https://adventofcode.com/2020/day/1
import sys

TARGET_VALUE = 2020

file = open(sys.argv[1], 'r')
input = file.readlines()
total = len(input)

for i in range(0, total):
    firstNum = int(input[i])
    
    for j in range (i + 1, total):
        secondNum = int(input[j])

        if firstNum + secondNum == TARGET_VALUE:
            print("{} * {} = {}".format(firstNum, secondNum, firstNum * secondNum))
            break
        elif firstNum + secondNum > TARGET_VALUE:
            # Don't search for third number when alredy two numbers have exceeded target value
            continue

        for k in range(j + 1, total):
            thirdNum = int(input[k])

            if firstNum + secondNum + thirdNum == TARGET_VALUE:
                print("{} * {} * {} = {}".format(firstNum, secondNum, thirdNum, firstNum * secondNum * thirdNum))
                exit(0)

file.close()