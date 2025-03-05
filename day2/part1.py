import sys

def Day2(input = "input.txt"):
    safeCounter = 0
    with open(input, "r") as f:
        for line in f:
            try:
                safe = True
                nums = list(map(int, line.split()))

                # Base cases
                if (len(nums) < 2):
                    safe+= 1
                    continue
                if(nums[0] == nums[1]):
                    continue
        
                ## check if they should always be increasing or decreasing
                isIncreasing = nums[0] < nums[1]
                for i in range(len(nums) - 1):
                    first = nums[i]
                    second = nums[i+1] 
                    if isIncreasing:
                        if first >= second:
                            safe = False
                            break
                    else:
                        if first <= second:
                            safe = False
                            break
                    if abs(first - second) >= 4:
                            safe = False
                            break
                if safe:
                    safeCounter += 1
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
        

    return safeCounter

print(Day2())