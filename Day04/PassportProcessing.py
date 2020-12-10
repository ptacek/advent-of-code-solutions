# https://adventofcode.com/2020/day/4
import sys
import re

lines = open(sys.argv[1], 'r').readlines()
validKeys = 0
validValues = 0
passport = {}

def validateHeight(value):
    match = re.search("^([0-9]+)(in|cm)$", value)

    if not match:
        return False

    height = int(match.group(1))
    unit = match.group(2)

    if unit == 'cm':
        return True if height >= 150 and height <= 193 else False
    else:
        return True if height >= 59 and height <= 76 else False

# Required passowrd keys and their validation rules
rules = {
    'byr': lambda x: int(x) >= 1920 and int(x) <= 2002, 
    'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020, 
    'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030, 
    'hgt': validateHeight, 
    'hcl': lambda x: re.match("^#[0-9a-f]{6}$", x) is not None, 
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
    'pid': lambda x: re.match("^[0-9]{9}$", x) is not None
}

# Does passport contain all mandatory keys?
def validatePassportKeys(passport):
    passportKeys = set(passport.keys())

    return len(rules) == len(passportKeys.intersection(rules.keys()))

# Are all passport values valid?
def validatePassportRules(passport):
    for key in passport:
        if key == 'cid':
            continue

        rule = rules[key]
        value = passport[key]

        if rule(value) is not True:
            return False

    return True

def parsePassportLine(line):
    values = map(lambda x: tuple(x.split(":")), line.strip().split(" "))
    
    return list(values)

# Check if password contains mandatory keys (part 1) and if
# all values are valid (part 2) and return incremented counters of 
# valid passports
def validateAndCountPassport(passport, validKeys, validValues):
    if validatePassportKeys(passport) is not True:
        return (validKeys, validValues)
    elif validatePassportRules(passport) is not True:
        return (validKeys + 1, validValues)
    else:
        return (validKeys + 1, validValues + 1)

for line in lines:
    if line == '\n':
        # Separator of passports
        validKeys, validValues = validateAndCountPassport(passport, validKeys, validValues)
        passport = {}
        continue

    passport.update(parsePassportLine(line))

# Validate last passport
validKeys, validValues = validateAndCountPassport(passport, validKeys, validValues)

print("Passports with valid keys: {}".format(validKeys))
print("Valid passports: {}".format(validValues))

