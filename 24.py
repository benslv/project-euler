import itertools

num = "0123456789"

perms = ["".join(perm) for perm in itertools.permutations(num)]

print(perms[999999])
