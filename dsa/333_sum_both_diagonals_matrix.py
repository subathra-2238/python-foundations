matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

main_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(n):
    main_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][n - 1 - i]

print("Main diagonal sum:", main_diagonal_sum)
print("Secondary diagonal sum:", secondary_diagonal_sum)
