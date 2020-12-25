import sys
from collections import deque

def calculateScore(winner):
    score = 0
    i = 1

    while len(winner) > 0:
        score += winner.pop() * i
        i += 1

    return score

def parseDecks(lines):
    player1 = deque()
    player2 = deque()
    nextPlayer = False

    for line in lines:
        if line.strip() == "":
            nextPlayer = True
            continue
        elif line.startswith("Player"):
            continue
        elif nextPlayer is True:
            player2.append(int(line))
        else:
            player1.append(int(line))

    return (player1, player2)

def play(player1, player2):
    while len(player1) != 0 and len(player2) != 0:
        card1 = player1.popleft()
        card2 = player2.popleft()

        if (card1 > card2):
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)

    if len(player1) == 0:
        return calculateScore(player2)
    else:
        return calculateScore(player1)

file = open(sys.argv[1], 'r')
lines = file.readlines()

player1, player2 = parseDecks(lines)
score = play(player1, player2)

print("Winner's score is {}".format(score))

file.close()