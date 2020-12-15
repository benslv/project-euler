from itertools import combinations_with_replacement


def divisors(n):
    return [x for x in range(1, n) if n % x == 0]


# First, calculate a list of all abundant numbers up to 28123.
abundants = set(n for n in range(1, 28124) if sum(divisors(n)) > n)

abundant_sums = set(map(sum, combinations_with_replacement(abundants, 2)))

print("Finished generating abundant sums!")
print("Beginning search...")

ans = 0
for n in range(28124):
    if n not in abundant_sums:
        ans += n

print(ans)
