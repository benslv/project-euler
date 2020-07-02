import math

num = math.factorial(100)

num_length = math.floor(math.log(num, 10))

print(num)
print(num_length)

total = sum(list(map(int, str(num))))

print(total)
