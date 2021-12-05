#https://adventofcode.com/2021/day/5
import sys
import functools

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Parses text input into list of line objects
def parseLines(input):
    lines = []

    for row in input:
        row = row.strip().split(" -> ")
        line = Line(tuple(map(lambda x: int(x), row[0].split(','))),
                    tuple(map(lambda x: int(x), row[1].split(','))))
        lines.append(line)
    
    return lines

# Initializes empty diagram based on maximum of x,y dimensions
def initDiagram(lines):
    xMax = 0
    yMax = 0

    xMax = max(map(lambda line: max(line.start[0], line.end[0]), lines))
    yMax = max(map(lambda line: max(line.start[1], line.end[1]), lines))
    
    diagram = []
    
    for i in range(0, yMax + 1):
        diagram.append([0] * (xMax + 1))
    
    return diagram

def drawVerticalLine(diagram, line):
    x = line.start[0]
    yStart = min(line.start[1], line.end[1])
    yEnd = max(line.start[1], line.end[1])

    for y in range(yStart, yEnd + 1):
        diagram[y][x] += 1

def drawHorizontalLine(diagram, line):
    y = line.start[1]
    xStart = min(line.start[0], line.end[0])
    xEnd = max(line.start[0], line.end[0])

    for x in range(xStart, xEnd + 1):
        diagram[y][x] += 1

def drawDiagonalLine(diagram, line):
    x = line.start[0]
    y = line.start[1]
    xEnd = line.end[0]
    yEnd = line.end[1]

    while (True):
        diagram[y][x] += 1

        if (x == xEnd):
            break

        if x < xEnd:
            x += 1
        else:
            x -= 1

        if y < yEnd:
            y += 1
        else:
            y -= 1
        
# Draws lines into diagram (increases counters on individual points)
def drawLines(diagram, lines, diagonals):
    for line in lines:
        if line.start[0] == line.end[0]:
            drawVerticalLine(diagram, line)
        elif line.start[1] == line.end[1]:
            drawHorizontalLine(diagram, line)
        elif diagonals is True:
            drawDiagonalLine(diagram, line)

# Counts points in diagram, where overlap counter is >= 2
def countDangerousPoints(diagram):
    return functools.reduce(
            lambda a, line: a + len(list(filter(lambda x: x > 1, line))), 
            diagram,
            0
           )

# Runs the algorithm. Parameter 'diagonals' is used for running part one or two of the puzzle
# With diagonals = True also diagonal lines are counted
def run(lines, diagonals):
    diagram = initDiagram(lines)
    drawLines(diagram, lines, diagonals)
    danger = countDangerousPoints(diagram)
    print(f"There are {danger} dangerous points")

file = open(sys.argv[1], 'r')
input = file.readlines()
lines = parseLines(input)

print("Part one (horizontal, vertical):")
run(lines, False)

print("\nPart two (horizontal, vertical, diagonal):")
run(lines, True)

file.close()