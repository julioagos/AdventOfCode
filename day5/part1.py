import sys


# based on a line of numbers and rules. Check if it follows the rules
def checkRules(line, rules):
    seen = set({})
    for num in line:
        seen.add(num)
        if rules.get(num):
            for value in rules[num]:
                if value in seen:
                    return False
    return True

def Day5(input = "input.txt"):
    sum = 0
    nums = []
    rules = {}
    with open(input, "r") as f:
        for line in f:
            try:
                if '|' in line:
                    num1, num2 = line.strip().split("|")
                    if rules.get(int(num1)):
                        rules[int(num1)].append(int(num2))
                    else:
                        rules[int(num1)] = [int(num2)]
                elif line.strip():
                    print(line)
                    nums.append(list(map(int, line.split(','))))
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
    for line in nums:
        if checkRules(line, rules):
            midPoint = len(line) // 2
            sum += line[midPoint]
        
    return sum

print(Day5())