import sys
from collections import defaultdict, deque


def findGuard(field) -> tuple[int, int]:
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == '^':
                return x, y
            
def moveForward(x,y,direction,field):
    sum = 0
    directionMap = {
        "u":    [-1, 0], # Up
        "d":    [1, 0],  # Down
        "l":    [0, -1], # Left
        "r":    [0, 1],  # Right
    }
    dir = directionMap[direction]
    while True:
        x += dir[1]
        y += dir[0]
        
        # Exited the field
        if x < 0 or x >= len(field[0]): # assumes every line is the same length
            return x,y, sum, True
        elif y < 0 or y >= len(field):
            return x,y, sum, True
        
        cur = field[y][x]
        # went into new space
        if cur == '.' or cur == '^':
            sum += 1
            
            # Convert the specific string (field[y]) to a list of characters to sub one char
            field_list = list(field[y])
            field_list[x] = 'X'
            field[y] = ''.join(field_list)
            continue
        # found obstruction
        elif cur == '#':
            return x - dir[1], y-dir[0], sum, False
        
        ## already been here so continue
        elif cur == "X":
            continue
    
        
        

def Day6(input = "input.txt"):
    # one for the guard starting position
    sum = 1
    field = []
    directions = [
        "u",
        "r",
        "d",
        "l",
    ]
    with open(input, "r") as f:
        for line in f:
            try:
                field.append(line.strip())
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
    x,y = findGuard(field)
    field_list = list(field[y])
    field_list[x] = 'X'
    field[y] = ''.join(field_list)
    
    exited = False
    while not exited:
        for i in range(len(directions)):
            x, y, visited, exited = moveForward(x,y, directions[i], field)
            sum += visited
            if exited:
                break
            
    return sum

print(Day6())