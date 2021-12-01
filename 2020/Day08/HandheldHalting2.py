import sys

# Parses input into list of commands + list of indexes with NOP and JMP commands
def parseCommands(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    commands = []
    changes = []

    for idx, line in enumerate(lines):
        tmp = line.strip().split(" ")
        commands.append({"command": tmp[0], "value": int(tmp[1]), "executed": False})
        
        if (tmp[0] in ["nop", "jmp"]):
            changes.append(idx)
    
    file.close()

    return (commands, changes)

# Changes NOP command for JMP or vice versa
def makeChange(cmd):
    if cmd['command'] == 'nop':
        cmd['command'] = 'jmp'
    else:
        cmd['command'] = 'nop'

# Set command as not executed for another retries
def resetCommand(cmd):
    cmd['executed'] = False
    return cmd

# Tries to run list of commands. Returns acc value or None in case of infinite loop
def runProgram(commands):
    acc = 0
    i = 0

    while True:
        if commands[i]['executed'] is True:
            # Infinite loop detected
            return None

        command = commands[i]['command']
        commands[i]['executed'] = True
        
        if command == 'nop':
            i += 1
        elif command == 'acc':
            acc += commands[i]['value']
            i += 1
        elif command == 'jmp':
            i += commands[i]['value']

        if i == len(commands):
            # Successful end of program
            return acc

commands, changes = parseCommands(sys.argv[1])
acc = None

# Tries to change instruction until the program returns valid value
while acc is None and len(changes) > 0:
    commands = [resetCommand(cmd) for cmd in commands]
    changeIndex = changes.pop()
    makeChange(commands[changeIndex])

    acc = runProgram(commands)

    # Revert change and try another in next iteration
    makeChange(commands[changeIndex])


print("Acc: {}".format(acc))