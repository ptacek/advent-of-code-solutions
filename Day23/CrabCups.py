# Node of a linked list
class Cup:
    def __init__(self, label):
        self.label = label
        self.next = None

# Parses line of numbers into circular linked list of cups + continues to 1million of cups
def parseCups(line, additionalCups):
    current = Cup(int(line[0]))
    prev = current
    pointers = {current.label: current}

    for number in line[1:]:
        cup = Cup(int(number))
        pointers[cup.label] = cup
        prev.next = cup
        prev = cup

    maxLabel = int(max(line))

    for number in range(maxLabel + 1, additionalCups + 1):
        cup = Cup(number)
        pointers[cup.label] = cup
        prev.next = cup
        prev = cup
        maxLabel = number

    cup.next = current

    return (current, pointers, maxLabel)

# Removes three nodes (cups) after the current node from the linked list
def pickupCups(cup, pointers):
    first = cup
    firstPicked = cup.next

    for i in range(0, 3):
        cup = cup.next
        del pointers[cup.label]
    
    first.next = cup.next
    cup.next = firstPicked

    return firstPicked

# Selects destination cup - current cup label - 1 if present in current list. Starts
# again from maximum value when 0 is reached
def selectDestination(cup, pointers, maxLabel):
    destLabel = cup.label - 1

    while destLabel not in pointers:
        destLabel -= 1

        if destLabel < 1:
            destLabel = maxLabel

    return pointers[destLabel]

# Returns picked cups (removed nodes) after destination node
def returnCups(dest, picked, pointers):
    next = dest.next
    dest.next = picked
    pointers[picked.label] = picked

    for i in range(0, 2):
        picked = picked.next
        pointers[picked.label] = picked

    picked.next = next

# PART ONE Result
# Traverses cups after cup 1 and prints their labels in a row
def printCups(cup):
    while cup.label != 1:
        cup = cup.next

    cup = cup.next
    text = ""

    while cup.label != 1:
        text += str(cup.label)
        cup = cup.next

    print(text)

# PART TWO result
# Traverses list until label 1 is found and then prints multiplication of next 2 nodes
def printMultiplication(cup):
    while cup.label != 1:
        cup = cup.next

    cup = cup.next
    label1 = cup.label
    cup = cup.next

    print(label1 * cup.label)

def playGame(input, rounds, additionalCups):
    currentCup, pointers, maxValue = parseCups(list(input), additionalCups)

    for i in range(0, rounds):
        picked = pickupCups(currentCup, pointers)
        dest = selectDestination(currentCup, pointers, maxValue)
        returnCups(dest, picked, pointers)
        currentCup = currentCup.next

    return currentCup

input = "586439172"

# PART ONE
currentCup = playGame(input, 100, 0)
printCups(currentCup)

#PART TWO
currentCup = playGame(input, 10000000, 1000000)
printMultiplication(currentCup)

