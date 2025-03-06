import sys

def Day4(input = "input.txt"):
    sum = 0
    strs = []
    directions = [
        [-1, 0], # Up
        [1, 0],  # Down
        [0, -1], # Left
        [0, 1],  # Right
        [-1, -1], # Top-left diagonal
        [-1, 1],  # Top-right diagonal
        [1, -1],  # Bottom-left diagonal
        [1, 1],   # Bottom-right diagonal
    ]
    with open(input, "r") as f:
        for line in f:
            try:
                strs.append(line.strip())
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
    for y in range(len(strs)):
        for x in range(len(strs[y])):
            if strs[y][x] == 'X':
                for direction in directions:
                    if check_direction(direction, strs, x,y):
                        sum += 1
    return sum

def check_direction(dir, strs, x,y) -> bool:
    toFind = "MAS"
    for i in range(3):
        x += dir[1]
        y += dir[0]
        if x < 0 or x >= len(strs[0]): # assumes every line is the same length
            return False
        elif y < 0 or y >= len(strs):
            return False
        elif strs[y][x] != toFind[i]:
            return False
    return True

print(Day4())