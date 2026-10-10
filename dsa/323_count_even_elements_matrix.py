matrix = [
    [10, 25, 14],
    [7, 20, 31],
    [5, 36, 42]
]

count = 0

for row in matrix:
    for number in row:
        if number % 2 == 0:
            count += 1

print("Number of even elements:", count)
