import re
import sys

def Day3(input = "input.txt"):
    sum = 0
    with open(input, "r") as f:
        for line in f:
            try:
                # Regex pattern to match find all instances of mul(X,Y) and pull out X and Y
                pattern = r"mul\((-?\d+),(-?\d+)\)"
                ops = re.findall(pattern, line)
                for op in ops:
                    
                    sum += int(op[0]) * int(op[1])
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
    return sum
print(Day3())