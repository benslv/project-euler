def d(n):
    return sum([i for i in range(1, n) if n % i == 0])

amicable = set()

for a in range(1, 10000):
    if a in amicable:
        continue

    a_val = d(a)

    if d(a_val) == a and a != a_val:
        amicable.update([a, a_val])

print(sum(amicable))