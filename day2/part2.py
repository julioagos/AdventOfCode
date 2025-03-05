import sys

## returns -1 is line is safe. If it's not safe, return where check failed.
def isSafe(nums) -> int:

    #base cases
    if len(nums) < 2:
        return -1
    if(nums[0] == nums[1]):
        return 0

    ## check if they should always be increasing or decreasing
    isIncreasing = nums[0] < nums[1]
    for i in range(len(nums) - 1):
        first = nums[i]
        second = nums[i+1] 
        if isIncreasing:
            if first >= second:
                return i
        else:
            if first <= second:
                return i
        if abs(first - second) >= 4:
                return i
    return -1


def Day2P2(input = "input.txt"):
    safeCounter = 0
    with open(input, "r") as f:
        for line in f:
            try:
                nums = list(map(int, line.split()))
                fault = isSafe(nums)
                if(fault == -1):
                    safeCounter +=1
                else:
                    ## try removing the faulty indices
                    if isSafe(nums[:fault] + nums[fault+1:]) == -1:
                        safeCounter+= 1
                    elif isSafe(nums[:fault+1] + nums[fault+2:]) == -1:
                        safeCounter+= 1
                    ## edge case where the first one is the problem argument and the isIncreasing doesn't match
                    elif fault != 0:
                        if isSafe(nums[1:]) == -1:
                            safeCounter+= 1
                
            except Exception as e:
                print(f"Unable to parse input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
        

    return safeCounter

print(Day2P2())