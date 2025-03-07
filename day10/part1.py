import sys
from collections import deque


def bfs(field, startX, startY):
    # Directions for moving
    directions = [
        (-1, 0), 
        (1, 0), 
        (0, -1), 
        (0, 1)
    ]

    yLimit, xLimit = len(field), len(field[0])
    
    # Initialize BFS queue and visited set
    queue = deque([(startY, startX)])
    visited = set([(startY, startX)])
    sum = 0
    
    # Start BFS
    while queue:
        y, x = queue.popleft()
        # If we are at a 9, increment the count of reachable nines
        if field[y][x] == 9:
            sum += 1
            continue
        
        # Explore the four possible directions
        for y2, x2 in directions:
            newY, newX = y + y2, x + x2
            if 0 <= newY and newY < yLimit and 0 <= newX and newX < xLimit:
                if (newY, newX) not in visited:
                    if field[newY][newX] == field[y][x] + 1:
                        visited.add((newY, newX))
                        queue.append((newY, newX))
    
    return sum

def Day10(input = "input.txt"):
    field=[]
    sum=0
    with open(input, "r") as f:
        for line in f:
            try:
                field.append(list(map(int,list(line.strip()))))
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)

    y, x = len(field), len(field)
    
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 0:
                sum += bfs(field, x, y)
    
    return sum

print(Day5())