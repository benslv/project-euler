def sum_of_digits(n):
    return sum(list(map(int, str(n))))


print(sum_of_digits(2**1000))
