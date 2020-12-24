import sys

# Parse line into list of numbers, operators and parentheses
def tokenize(line):
    tokens = []
    token = ""

    for char in line:
        if char in ['+', '*', '(', ')']:
            if token != "":
                tokens.append(int(token))
                token = ""
            tokens.append(char)
        else:
            token += char

    if token != "":
        tokens.append(int(token))

    return tokens

# PART ONE
# Alrgorithm for converting infix notation to postifx, but simplified and reversed
# because all operators have the same precedence in left to right order 
def toPostfixPartOne(tokens):
    output = []
    stack = []
    
    for token in reversed(tokens):
        if type(token) is int:
            output.append(token)
        elif token == ')':
            stack.append(token)
        elif token in ['*', '+']:
            stack.append(token)
        elif token == '(':
            while True:
                op = stack.pop()

                if op == ')':
                    break
                else:
                    output.append(op)

    while len(stack) > 0:
        output.append(stack.pop())

    return output

# Converts parsed tokens to postfix notation and evalutes it using stack
def evaluate(tokens, algorithm):
    postfix = algorithm(tokens)
    stack = []

    for token in postfix:
        if type(token) is int:
            stack.append(token)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '+':
            stack.append(stack.pop() + stack.pop())

    return stack.pop()

file = open(sys.argv[1], 'r')
lines = file.readlines()

sum = 0

for line in lines:
    tokens = tokenize(line.replace(" ", "").strip())
    sum += evaluate(tokens, toPostfixPartOne)

print("I: Sum of all expressions is {}".format(sum))

file.close()