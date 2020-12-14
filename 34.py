import math

i = 10  # start at 1 because any number below cannot contain a sum of digits


def splitNum(n):
    digits = []
    while n > 0:
        digits.insert(0, n % 10)  # add ones digit to front of digits
        n = n // 10
    return digits


nums = []

# Upper limit is this
while i <= 40585:
    digits = splitNum(i)
    n = sum(map(math.factorial, digits))
    if i == n:
        nums.append(i)
    i += 1

print(nums)