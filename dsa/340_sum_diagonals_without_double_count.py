matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

total = 0

for i in range(n):
    total += matrix[i][i]
    total += matrix[i][n - 1 - i]

if n % 2 == 1:
    total -= matrix[n // 2][n // 2]

print("Sum of both diagonals:", total)
