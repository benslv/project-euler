def find_period(n):
    rem = 1 % n

    if rem == 0:
        return 0

    values = set()

    while rem not in values and len(values) < n-1:
        values.add(rem)
        rem *= 10
        rem %= n

        # print("rem", rem)
        # print("values", values)

    return len(values)


# print(find_period(3))

d = 1000
max_period = 0

while d > 0:
    if (max_period >= d):
        d += 1
        break

    period = find_period(d)
    max_period = max(period, max_period)

    print(f"{d} has a repeating {period} digits.")

    d -= 1


print(
    f"Number with the longest repeating period was {d}, with a period of {max_period} digits.")
