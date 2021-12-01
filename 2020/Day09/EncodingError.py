import sys

def hasSum(numbers, targetValue):
    for i in range(0, len(numbers)):
        iVal = int(numbers[i])

        for j in range(i + 1, len(numbers)):
            jVal = int(numbers[j])

            if iVal + jVal == targetValue:
                return True

    return False

# Part ONE
def findInvalidValue(numbers, preamble):
    for i in range(preamble, len(numbers)):
        number = int(lines[i])
        previous = lines[i-preamble:i]

        if hasSum(previous, number) == False:
            return number

# Part TWO
def findCodeWeakness(lines, targetValue):
    for i in range(0, len(lines)):
        iVal = int(lines[i])
        j = i
        sum = iVal
        minVal = iVal
        maxVal = iVal

        while sum < targetValue:
            j += 1
            jVal = int(lines[j])
            sum += jVal
            minVal = jVal if jVal < minVal else minVal
            maxVal = jVal if jVal > maxVal else maxVal

            if sum == targetValue:
                return minVal + maxVal
            elif sum > targetValue:
                break


file = open(sys.argv[1], 'r')
lines = file.readlines()

invalidValue = findInvalidValue(lines, 25)
weakness = findCodeWeakness(lines, invalidValue)

print("Invalid value is {}, encryption weakness is {}".format(invalidValue, weakness))

file.close()