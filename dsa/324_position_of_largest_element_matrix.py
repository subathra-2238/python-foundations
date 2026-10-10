matrix = [
    [10, 25, 15],
    [40, 20, 30],
    [5, 35, 45]
]

largest = matrix[0][0]
largest_row = 0
largest_column = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > largest:
            largest = matrix[i][j]
            largest_row = i
            largest_column = j

print("Largest element:", largest)
print("Row:", largest_row + 1)
print("Column:", largest_column + 1)
