matrix = [
    [10, 25, 15],
    [40, 20, 30],
    [5, 35, 45]
]

for row in matrix:
    largest = row[0]

    for number in row:
        if number > largest:
            largest = number

    print("Largest element:", largest)
