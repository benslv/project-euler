import math

with open("13.txt", "r") as f:
    nums = list(map(int, f.read().splitlines()))

# total = 0
# for num in nums:
#     total += num // (10 ** 42)

# print(total)

print(sum(nums))
