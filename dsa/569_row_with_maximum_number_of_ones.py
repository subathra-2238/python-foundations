
def row_with_max_ones(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    max_ones = 0
    answer = -1

    for i in range(rows):
        low = 0
        high = cols - 1
        first_one = cols

        # Binary search for the first occurrence of 1
        while low <= high:
            mid = (low + high) // 2

            if matrix[i][mid] == 1:
                first_one = mid
                high = mid - 1
            else:
                low = mid + 1

        ones = cols - first_one

        if ones > max_ones:
            max_ones = ones
            answer = i

    return answer


matrix = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 1]
]

print("Row with maximum ones:", row_with_max_ones(matrix))
