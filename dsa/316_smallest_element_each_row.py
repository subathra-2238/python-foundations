matrix = [
    [10, 25, 15],
    [40, 20, 30],
    [5, 35, 45]
]

for row in matrix:
    smallest = row[0]

    for number in row:
        if number < smallest:
            smallest = number

    print("Smallest element:", smallest)
