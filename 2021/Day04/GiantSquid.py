#https://adventofcode.com/2021/day/4
import sys
import re

BOARD_SIZE = 5

# Reads text input into list of boards => 3-dimensional list
def readBoards(input):
    boards = []
    board = []

    for line in input:
        line = line.strip()

        if line == '':
            boards.append(board)
            board = []
            continue
        
        board.append(re.split('\s+', line))

    boards.append(board)

    return boards

# If bingo value and board value are the same, then adds mark to the column and row (increses counter)
# If row or column counter is equal to board size, then the board is winner
# Returns True if board has bingo, otherwise false
# i = board index, j = row index, k = column index
def markResult(marks, resValue, boardValue, i, j, k):
    if (resValue != boardValue):
        return
    
    rowKey = f"{i}:{j}"
    colKey = f"{i}:{k}"

    if rowKey in marks['rows']:
        marks['rows'][rowKey] += 1
    else:
        marks['rows'][rowKey] = 1

    if colKey in marks['cols']:
        marks['cols'][colKey] += 1
    else:
        marks['cols'][colKey] = 1

    if marks['rows'][rowKey] == BOARD_SIZE or marks['cols'][colKey] == BOARD_SIZE:
        return True
    else:
        return False

# Calculates score from winning board based on non-marked numbers on board
def calculateScore(board, results):
    sum = 0
    winningNumber = int(results[-1])
    
    for row in board:
        for num in row:
            if num not in results:
                sum += int(num)

    return sum * winningNumber

# Fills bingo results into boards. If board has bingo, calculates its score
# Returns dictionary of winners and their score.
def fillResults(boards, results):
    marks = {'cols': {}, 'rows': {}}
    winners = {}

    for resIdx, res in enumerate(results):
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                for k, col in enumerate(line):
                    winner = markResult(marks, res, boards[i][j][k], i, j, k)
                    
                    if winner is True and i not in winners:
                        winners[i] = calculateScore(board, results[:resIdx + 1])

    return winners

file = open(sys.argv[1], 'r')
input = file.readlines()

results = input[0].strip().split(',')
boards = readBoards(input[2:])
winners = fillResults(boards, results)

# First winner's score is result of PART ONE
# Last "winner's" score is result of PART TWO 
for order, board in enumerate(winners):
    print(f"{order + 1}. {board}: {winners[board]}")

file.close()