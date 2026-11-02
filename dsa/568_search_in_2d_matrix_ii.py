
def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        current = matrix[row][col]

        if current == target:
            return True

        elif current > target:
            # Move left to find a smaller value
            col -= 1

        else:
            # Move down to find a larger value
            row += 1

    return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

target = 5

print("Target found:", search_matrix(matrix, target))
