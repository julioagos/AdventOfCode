import sys

def Day1(input = "input.txt"):
    nums1 = []
    nums2 = []

    with open(input, "r") as f:
        for line in f:
            try:
                num1, num2 = line.split()
                nums1.append(int(num1))
                nums2.append(int(num2))
            except Exception as e:
                print(f"Unable to read input file. Couldn't parse: {line}Error: {e}" + line)
                sys.exit(1)

    nums1.sort()
    nums2.sort()
    sum = 0

    for i in range(len(nums1)):
        sum += abs(nums1[i] - nums2[i])
    return sum

print(Day1())