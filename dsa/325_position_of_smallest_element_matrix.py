matrix = [
    [10, 25, 15],
    [40, 20, 30],
    [5, 35, 45]
]

smallest = matrix[0][0]
smallest_row = 0
smallest_column = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < smallest:
            smallest = matrix[i][j]
            smallest_row = i
            smallest_column = j

print("Smallest element:", smallest)
print("Row:", smallest_row + 1)
print("Column:", smallest_column + 1)
