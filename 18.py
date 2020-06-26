with open("18.txt", "r") as f:
    arr = [list(map(int, x.split())) for x in f.read().splitlines()]

print(arr)

for row in range(len(arr) - 2, -1, -1):
    for col in range(len(arr[row])):
        print(row, col)
        arr[row][col] += max(arr[row+1][col], arr[row+1][col+1])

print(arr)
