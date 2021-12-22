#https://adventofcode.com/2021/day/16
import sys

# One packet with its version, type and literal value OR subpackets
class Packet:
    def __init__(self, version, typeId):
        self.version = version
        self.typeId = typeId
        self.sub = []
        self.literal = None

    # Sums version numbers of the packet and its subpackets
    def sumVersions(self):
        sum = self.version

        for sub in self.sub:
            sum += sub.sumVersions()

        return sum
    
    # Evalutes the expression of the packet
    # (would be better with class inheritance, but i don't want to write so many subclasses just for puzzle)
    def evaluate(self):
        if self.typeId == 0:
            sum = 0

            for sub in self.sub:
                sum += sub.evaluate()

            return sum
        
        if self.typeId == 1:
            product = 1

            for sub in self.sub:
                product *= sub.evaluate()

            return product

        if self.typeId == 2:
            min = None

            for sub in self.sub:
                val = sub.evaluate()
                min = val if min is None or min > val else min

            return min

        if self.typeId == 3:
            max = None

            for sub in self.sub:
                val = sub.evaluate()
                max = val if max is None or max < val else max

            return max

        if self.typeId == 4:
            return self.literal

        if self.typeId == 5:
            return 1 if self.sub[0].evaluate() > self.sub[1].evaluate() else 0

        if self.typeId == 6:
            return 1 if self.sub[0].evaluate() < self.sub[1].evaluate() else 0

        if self.typeId == 7:
            return 1 if self.sub[0].evaluate() == self.sub[1].evaluate() else 0

# Converts hexa string to bin string (one hexa char to 4 binary digits)
def convertToBin(input):
    binary = ""

    for i in range(0, len(input)):
        number = "000" + bin(int(input[i], 16))[2:]
        binary += number[-4:]

    return binary

# Decodes packet content as a literal value
def decodeLiteralPacket(packet, input, i):
    number = ""

    while True:
        word = input[i:i+5]
        i += 5
        number += word[1:]

        if word[0] == '0':
            break
    
    packet.literal = int(number, 2)

    return (packet, i)

# Decodes subpackets with given their length as the first 15 bits
def decodeSubpacketsWithLength(packet, input, i):
    length = int(input[i : i + 15], 2)
    i += 15
    packetEnd = i + length

    while i < packetEnd:
        subPacket, i = decodePacket(input, i, True)
        packet.sub.append(subPacket)

    return (packet, i)

# Decodes subpackets with given their number as the first 11 bits
def decodeSubpacketsWithNumber(packet, input, i):
    number = int(input[i : i + 11], 2)
    i += 11

    for j in range(0, number):
        subPacket, i = decodePacket(input, i, True)
        packet.sub.append(subPacket)

    return (packet, i)

# Decodes operator packet in one of the possible ways, specified in the first bit
def decodeOperatorPacket(packet, input, i):
    lengthType = input[i]
    i += 1

    if lengthType == '0':
        return decodeSubpacketsWithLength(packet, input, i)
    else:
        return decodeSubpacketsWithNumber(packet, input, i)

# Creates packet with decoded version and type ID
# Then decodes its content based on the type id 
def decodePacket(input, i, subPacket):
    packet = Packet(int(input[i:i+3], 2), int(input[i+3:i+6], 2))
    i += 6
    
    if packet.typeId == 4:
        packet, i = decodeLiteralPacket(packet, input, i)
    else:
        packet, i = decodeOperatorPacket(packet, input, i)

    # skip padding at the end if it's not a sub-packet
    i = i + ((4 - i) % 4) if subPacket is False else i

    return (packet, i)

# MAIN:
file = open(sys.argv[1], 'r')
input = file.readlines()[0].strip()

i = 0
sum = 0

input = convertToBin(input)
packet, i = decodePacket(input, i, False)

print(f"I: sum of all packet's versions is {packet.sumVersions()}")
print(f"II: result of the packet's expression {packet.evaluate()}")


file.close()