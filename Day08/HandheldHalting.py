import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

commands = []

for line in lines:
    tmp = line.strip().split(" ")
    commands.append({"command": tmp[0], "value": int(tmp[1]), "executed": False})

acc = 0
i = 0

while True:
    if commands[i]['executed'] is True:
        break

    command = commands[i]['command']
    commands[i]['executed'] = True
    
    if command == 'nop':
        i += 1
    elif command == 'acc':
        acc += commands[i]['value']
        i += 1
    elif command == 'jmp':
        i += commands[i]['value']

print("Acc: {}".format(acc))

file.close()