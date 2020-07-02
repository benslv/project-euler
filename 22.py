with open("22.txt", "r") as f:
    names = enumerate(
        sorted(f.read().replace("\"", "").split(",")),
        1
    )

total = sum([sum([ord(c)-64 for c in name])*i for (i, name) in names])

print(total)
