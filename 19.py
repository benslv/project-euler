from datetime import date

num = 0
START_YEAR = 1901
END_YEAR = 2000

for i in range(START_YEAR, END_YEAR+1):
    for j in range(1, 13):
        if date(i, j, 1).weekday()  == 6:
            num += 1

print(num)