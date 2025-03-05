import sys

def Day1P2(input = "input.txt"):

    #array for the left and dict for the right
    nums1 = []
    nums2 = {}

    with open(input, "r") as f:
        for line in f:
            try:
                num1, num2 = line.split()
                nums1.append(int(num1))
                num2 = int(num2)

                # add 1 to the counter if already in the dict or set it to 1 if not in the dict
                if num2 in nums2:
                    nums2[num2] += 1
                else:
                    nums2[num2] = 1
            except Exception as e:
                print(f"Unable to read input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)
    sum = 0
    for i in range(len(nums1)):
        x = nums1[i]
        if x in nums2:
            sum += nums2[x] * x
    return sum

print(Day1P2())