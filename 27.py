import math

max_primes = {"n": 0, "a": 0, "b": 0}


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, math.floor(math.sqrt(n))):
        if (n % i == 0):
            return False

    return True


for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0

        while isPrime(n**2+a*n+b):
            n += 1

        if n > max_primes["n"]:
            max_primes.update({"n": n, "a": a, "b": b})

print(max_primes)
print(max_primes["a"]*max_primes["b"])
