def amicable(n):
    amicable = set()

    def pd(x): return [i for i in range(1, x) if x % i == 0]

    for a in range(1, n):
        if a in amicable:
            continue

        b = sum(pd(a))

        if sum(pd(b)) == a and a != b:
            amicable.update([a, b])

    return amicable


print(sum(amicable(10000)))
