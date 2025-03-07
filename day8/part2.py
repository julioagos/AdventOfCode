import sys

xlimit, ylimit = 0, 0

def modifyString(x,y, field, replacement):
    field_list = list(field[y])
    field_list[x] = replacement
    field[y] = ''.join(field_list)

def calculate_xy_distance(coord1, coord2):
    y = coord2[0] - coord1[0]
    x = coord2[1] - coord1[1]
    return y, x

def getPossibleAntinodeLocations(loc, x,y):
    possibleLocations = []
    
    #Backwards Direction 
    curY,curX = loc[0] -y, loc[1]-x
    while (curX < xlimit and curX >= 0) and (curY < ylimit and curY >= 0):
        possibleLocations.append([curY,curX])
        curY,curX = curY -y, curX -x
    
    # Forward Direction
    curY,curX = loc[0] + 2 * y, loc[1] + 2 * x
    while (curX < xlimit and curX >= 0) and (curY < ylimit and curY >= 0):
        possibleLocations.append([curY,curX])
        curY,curX = curY + y, curX + x
        
    return possibleLocations

def checkDistinct(coord, field):
    x, y = coord[1], coord[0]
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
        
    global xlimit, ylimit
    xlimit = len(lines[0])
    ylimit = len(lines)
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
            if checkDistinct(coords[i],lines):
                sum += 1
            for j in range(i+1,len(coords)):
                yDis, xDis = calculate_xy_distance(coords[i], coords[j])
                possibleLocations = getPossibleAntinodeLocations(coords[i], xDis, yDis)
                for p in possibleLocations:
                    if checkDistinct(p,lines):
                        sum += 1
    return sum

print(Day8())