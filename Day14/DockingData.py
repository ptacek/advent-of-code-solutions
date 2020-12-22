import sys
import re
import functools

def parseMask(text):
    raw = text.split(" = ")[1]

    return {
        "and": int(raw.replace("X", "1"), 2),
        "or": int(raw.replace("X", "0"), 2)
    }

def sumMemoryValues(memory):
    return functools.reduce(lambda a, b: a + b, memory.values())

file = open(sys.argv[1], 'r')
lines = file.readlines()
mask = None
pattern = re.compile("mem\[(\d+)\] = (\d+)")
memory = {}

for line in lines:
    if line.startswith("mask"):
        mask = parseMask(line.strip())
    else:
        print(line.strip())
        match = pattern.match(line.strip())
        addr = int(match.group(1))
        value = int(match.group(2))

        memory[addr] = value & mask['and'] | mask['or']

print(sumMemoryValues(memory))

file.close()