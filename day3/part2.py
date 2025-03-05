import sys
import re

def Day3P2(input = "input.txt"):
    sum = 0
    enabled = True
    with open(input, "r") as f:
        for line in f:
            try:
                # Regex pattern to match find all instances of mul(X,Y) and pull out X and Y. Also pulls out do's and don't
                pattern = r"mul\((-?\d+),(-?\d+)\)|(do\(\))|(don't\(\))"
                ops = re.findall(pattern, line)
                for op in ops:
                    ## found do
                    if op[2]:
                        enabled = True
                    ## found don't
                    elif op[3]:
                        enabled = False
                    elif op[0] and op[1]:
                        if enabled:
                            sum += int(op[0]) * int(op[1])
                    else:
                        print(f"Unknow expression found {op}")
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
    return sum
print(Day3P2())