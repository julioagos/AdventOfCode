import sys
from collections import defaultdict, deque


# based on a line of numbers and rules. Check if it follows the rules
def checkRules(line, rules) -> bool:
    seen = set({})
    for num in line:
        seen.add(num)
        if rules.get(num):
            for value in rules[num]:
                if value in seen:
                    return False
    return True

## fixes a line based on the rules using topological sort
def fixLine(nums, rules) -> list:
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    valid_nums = set(nums)
    
    # Fill adjacency list and in-degree counts from rules
    for x in rules:
        if x not in valid_nums:  # Skip numbers in rules that are not in nums
            continue
        for y in rules[x]:
            if y in valid_nums:
                adj_list[x].append(y)
                in_degree[y] += 1
                if y not in in_degree:
                    in_degree[y] = 0
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([num for num in nums if in_degree[num] == 0])
    sorted_list = []

    while queue:
        current = queue.popleft()
        sorted_list.append(current)

        # Decrease in-degree of all neighbors
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_list
    

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
        if not checkRules(line, rules):
            sorted = fixLine(line, rules)
            midPoint = len(line) // 2
            sum += sorted[midPoint]
        
    return sum

print(Day5())