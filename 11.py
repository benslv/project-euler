# Parse the input file and format it as a 2D list of ints.
with open("11.txt", "r") as f:
    f = [list(map(int, row.split(" "))) for row in f.read().splitlines()]

numbers_in_prod = 4
max_prod = 0

for row in range(len(f)):
    for col in range(row):
        # Check horizontally.
        # If there are enough columns between the current value and the edge of the grid.
        if (col < len(f[row]) - numbers_in_prod):
            prod = 1
            for i in range(col, col+numbers_in_prod):
                prod *= f[row][i]
            max_prod = prod if prod > max_prod else max_prod

        # Check vertically.
        if (row < len(f) - numbers_in_prod):
            prod = 1
            for i in range(row, row+numbers_in_prod):
                prod *= f[i][col]
            max_prod = prod if prod > max_prod else max_prod

        # Check diagonally down-right.
        if (row < len(f) - numbers_in_prod) and (col < len(f[row]) - numbers_in_prod):
            prod = 1
            for i in range(numbers_in_prod):
                prod *= f[row+i][col+i]
            max_prod = prod if prod > max_prod else max_prod

        # Check diagonally up-right.
        if (row < len(f) - numbers_in_prod) and (col < len(f[row]) - numbers_in_prod):
            prod = 1
            for i in range(numbers_in_prod):
                prod *= f[row-i][col+i]
            max_prod = prod if prod > max_prod else max_prod

print(max_prod)
