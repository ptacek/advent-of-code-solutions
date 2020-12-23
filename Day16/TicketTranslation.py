import sys
import functools

# Convert text rules to list of tuples of int numbers
def parseRule(text):
    return list(
        map(
            lambda x: tuple(
                map(
                    lambda y: int(y),
                    x.split("-")
                )
            ),
            text.split(" or ")
        )
    )

# parse lines with rules into dict
def parseRules(lines):
    rules = {}
    lineNr = 0

    for line in lines:
        if (line.strip() == ''):
            # end of rules
            return (rules, lineNr)
        else:
            tmp = line.strip().split(': ')
            rules[tmp[0]] = parseRule(tmp[1])
        lineNr += 1

# Convert text to list of int numbers
def parseTicket(line):
    return list(map(lambda x: int(x), line.strip().split(',')))


# parse rules, your ticket and nearby tickets
def parseInput(lines):
    rules, endLine = parseRules(lines)
    ticket = parseTicket(lines[endLine + 2])
    nearby = []

    for line in lines[endLine + 5:]:
        nearby.append(parseTicket(line))

    return (rules, ticket, nearby)

# Finds out if all values on ticket fullfils any rule
def validateTicket(ticket, rules):
    invalidValues = []

    for value in ticket:
        valid = False
        for ruleName in rules:
            for range in rules[ruleName]:
                if value >= range[0] and value <= range[1]:
                    valid = True
        
        if valid is not True:
            invalidValues.append(value)

    return invalidValues

# PART ONE
# Returns invalid values from tickets and filtered valid ony tickets
def validateValuesNearby(tickets, rules):
    invalidValues = []
    validTickets = []

    for ticket in tickets:
        invalid = validateTicket(ticket, rules)

        if len(invalid) > 0:
            invalidValues += invalid
        else:
            validTickets.append(ticket)
    
    return (invalidValues, validTickets)

# Initializes dictionary with indices of ticket values as keys and with set of all 
# possible rules as values
def initRules(exampleTicket, rules):
    columnRules = {}

    for idx in range(0, len(exampleTicket)):
        for rule in rules:
            if idx in columnRules:
                columnRules[idx].add(rule)
            else:
                columnRules[idx] = set([rule])
    
    return columnRules

# Takes column where only one rule is possible and removes the rule from
# other columns and repeats the process until there is only one rule
# for each column
def excludeRules(columnRules):
    sorted = []

    for key in columnRules:
        sorted.append((key, columnRules[key]))

    sorted.sort(key = lambda x: len(x[1]))
    
    for i, keyVal in enumerate(sorted):
        rule = next(iter(keyVal[1]))
        
        for other in sorted[i+1:]:
            other[1].remove(rule)

    result = {}

    for keyVal in sorted:
        result[keyVal[0]] = next(iter(keyVal[1]))

    return result

# PART TWO
# Validating values in all tickets and removing rules from dictionary of possible rules
# for each ticket column
def decodeTicketColumns(tickets, rules):
    columnRules = initRules(tickets[0], rules)

    for ticket in tickets:
        for idx, value in enumerate(ticket):
            for ruleName in rules:
                if ruleName not in columnRules[idx]:
                    continue

                valid = False

                for range in rules[ruleName]:
                    if value >= range[0] and value <= range[1]:
                        valid = True
                        break
                
                if valid == False:
                    columnRules[idx].remove(ruleName)

    return excludeRules(columnRules)

# Maps columns to ticket values
def mapTicket(ticketValues, ticketColums):
    ticket = {}

    for idx, value in enumerate(ticketValues):
        ticket[ticketColums[idx]] = value

    return ticket


file = open(sys.argv[1], 'r')
lines = file.readlines()

rules, ticket, nearby = parseInput(lines)

invalidValues, validTickets = validateValuesNearby(nearby, rules)
error = functools.reduce(lambda a,b : a + b, invalidValues, 0)

print("Ticket scanning error: {}".format(error))

ticketColums = decodeTicketColumns(validTickets, rules)
ticket = mapTicket(ticket, ticketColums)

# filter only departure columns and take only values
departureValues = list(map(lambda x: x[1], filter(lambda keyVal: keyVal[0].startswith("departure"), ticket.items())))
result = functools.reduce(lambda a,b: a * b, departureValues)

print("Result of part II is {}".format(result))

file.close()
