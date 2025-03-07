import sys


def modifyString(x,y, field, replacement):
    field_list = list(field[y])
    field_list[x] = replacement
    field[y] = ''.join(field_list)

def calculate_xy_distance(coord1, coord2):
    y = coord2[0] - coord1[0]
    x = coord2[1] - coord1[1]
    return y, x

def getPossibleAntinodeLocations(loc, x,y):
    possibleLocations = [[],[]]
    possibleLocations[0] = [loc[0] -y, loc[1]-x]                # Closer Node
    possibleLocations[1] = [loc[0] + 2 * y, loc[1] + 2 * x]     # Node that should be 2 * the distance
    return possibleLocations

def inField(coord, field):
    x, y = coord[1], coord[0]
    if y < len(field) and y >= 0:
        if x < len(field[y]) and x >= 0:
            if field[y][x] != '^':
                modifyString(x,y, field, '^') # Mark distinct location
                return True
    return False

def Day8(input = "input.txt"):
    sum = 0
    lines = []
    nodes = {}
    with open(input, "r") as f:
        for line in f:
            try:
                l = line.strip()
                lines.append(l)         
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
        
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            char = lines[y][x]
            if char != '.':
                if nodes.get(char):
                    nodes[char].append([int(y),int(x)])
                else:
                    nodes[char] = [[int(y),int(x)]]
    
    for node, coords in nodes.items():
        for i in range(len(coords)):
            for j in range(i+1,len(coords)):
                yDis, xDis = calculate_xy_distance(coords[i], coords[j])
                possibleLocations = getPossibleAntinodeLocations(coords[i], xDis, yDis)
                for p in possibleLocations:
                    if inField(p,lines):
                        print(p)
                        sum += 1
    
    return sum

print(Day8())