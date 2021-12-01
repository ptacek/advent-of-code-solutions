import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

count = 0
search = ["shiny gold"]
found = set()

while len(search) > 0:
    targetColor = search.pop()

    for line in lines:
        color = " ".join(line.split(" ")[:2])
        
        if color != targetColor and targetColor in line:
            found.add(color)
            search.append(color)
            

print("Count of unique bags: {}".format(len(found)))
file.close()