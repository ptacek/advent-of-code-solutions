import sys
import re

def parseRule(idx, rules):
    rule = rules[idx]

    if rule.startswith('"'):
        return rule.replace('"', '')

    vars = rule.split(" ")
    output = ""

    if '|' in vars:
        output += '('

    for var in vars:
        if var == ' ':
            continue
        elif var == '|':
            output += var
        else:
            output += parseRule(int(var), rules)

    if '|' in vars:
        output += ')'

    return output

def readInput(lines):
    rules = {}
    text = []
    readText = False

    for line in lines:
        if line.strip() == "":
            readText = True
            continue

        if readText:
            text.append(line.strip())
        else:
            tmp = line.strip().split(": ")
            rules[int(tmp[0])] = tmp[1]

    return (rules, text)

file = open(sys.argv[1], 'r')
lines = file.readlines()

rules, text = readInput(lines)
rule = '^' + parseRule(0, rules) + '$'
matching = 0

for line in text:
    match = re.match(rule, line)
    
    if match:
        matching += 1

print("{} lines are matching the rule 0".format(matching))

file.close()