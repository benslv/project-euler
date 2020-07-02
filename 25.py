import math

fib = [1, 1]

while math.floor(math.log(fib[-1], 10))+1 < 1000:
    fib.append(fib[-1]+fib[-2])

# print(sum([x for x in fib if x % 2 == 0]))
print(len(fib))
