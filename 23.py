def get_factors(n):
    factors = set()
    for i in range(1, int(n**0.5)+1):
        if (n % i == 0):
            factors.add(i)
            factors.add(n//i)

    return factors


def is_abundant(n):
    return sum(get_factors(n)) > n


nums = []

for i in range(1, 28124):
    for a in range(1, i):
        for b in range(1, i-a+1):
            # print(i, a, b)
            if sum([a, b]) == i and is_abundant(a) and is_abundant(b):
                break
        else:
            continue
        break

    nums.append(i)

print(nums)
