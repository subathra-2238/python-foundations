matrix = [
    [2, 4, 6],
    [1, 5, 7],
    [8, 3, 9]
]

trace = 0

for i in range(len(matrix)):
    trace += matrix[i][i]

print("Matrix trace:", trace)
