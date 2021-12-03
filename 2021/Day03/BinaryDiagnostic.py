#https://adventofcode.com/2021/day/3
import sys

file = open(sys.argv[1], 'r')
input = file.readlines()

# Returns how many zeros and how many ones there are on position X in given list of numbers
def getBitCounts(input, bitPosition):
    zeroCount = 0
    oneCount = 0

    for line in input:
        if int(line[bitPosition]) == 1:
            oneCount +=1
        else:
            zeroCount += 1
    
    
    return (zeroCount, oneCount)

# PART ONE result calculation
def getPowerConsumption(input):
    bitLen = len(input[0].strip())
    gamma = ""
    epsilon = ""

    for i in range(0, bitLen):
        zeroCount, oneCount = getBitCounts(input, i)

        if oneCount > zeroCount:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)

# Filters numbers in list that have given filter value on the given bit position 
def filterNumbers(numbers, bitPosition, filterValue):
    return list(filter(lambda num: int(num[bitPosition]) == filterValue, numbers))

# PART TWO - Oxygen generator rating calculation
def getOxygenRating(numbers):
    filterValueFunc = lambda zeroCnt, oneCnt: 1 if oneCnt >= zeroCnt else 0

    return getRating(numbers, filterValueFunc)

# PART TWO - CO2 scrubber rating rating calculation
def getCo2Rating(numbers):
    filterValueFunc = lambda zeroCnt, oneCnt: 0 if zeroCnt <= oneCnt else 1

    return getRating(numbers, filterValueFunc)

# Generic function for PART TWO result calculation
# oxygen or co2 depending on the function for selecting filter value
def getRating(numbers, filterValueFunc):
    bitLen = len(numbers[0])

    for i in range(0, bitLen):
        if len(numbers) == 1:
            break
    
        zeroCount, oneCount = getBitCounts(numbers, i)
        filterValue = filterValueFunc(zeroCount, oneCount)

        numbers = filterNumbers(numbers, i, filterValue)
    
    return int(numbers[0], 2)

# MAIN
power = getPowerConsumption(input)
print(f"Power consumption is {power}")

oxygen = getOxygenRating(input)
co2 = getCo2Rating(input)
print(f"Life support rating is {oxygen * co2}")

file.close()

