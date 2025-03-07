import sys

def checkPossibilities(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums
    
    if len(nums) == 2:
        return [nums[0] + nums[1], nums[0] * nums[1], concatNumbers(nums[0],nums[1])]
    
    return checkPossibilities([nums[0] + nums[1]] + nums[2:]) + checkPossibilities([nums[0] * nums[1]] + nums[2:]) + checkPossibilities([concatNumbers(nums[0],nums[1])] + nums[2:])

def concatNumbers(x,y):
    return int(str(x) + str(y))
    
    
def Day7(input = "input.txt"):
    sum = 0
    lines =[]
    with open(input, "r") as f:
        for line in f:
            try:
                lines.append(line)
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
        
        for line in lines:
            total = int(line.split(":")[0])
            nums = list(map(int, line.split()[1:]))
            x = checkPossibilities(nums)
            if total in x:
                sum += total
    return sum

print(Day7())