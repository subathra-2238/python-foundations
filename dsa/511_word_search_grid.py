
def word_search(board, word):
    rows = len(board)
    cols = len(board[0])

    def backtrack(row, col, index):
        if index == len(word):
            return True

        if (row < 0 or row >= rows or
                col < 0 or col >= cols):
            return False

        if board[row][col] != word[index]:
            return False

        # Mark this cell as visited
        original = board[row][col]
        board[row][col] = "#"

        found = (
            backtrack(row + 1, col, index + 1) or
            backtrack(row - 1, col, index + 1) or
            backtrack(row, col + 1, index + 1) or
            backtrack(row, col - 1, index + 1)
        )

        # Restore the original letter
        board[row][col] = original

        return found

    if not word:
        return True

    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, 0):
                return True

    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

print(word_search(board, "ABCCED"))
print(word_search(board, "SEE"))
print(word_search(board, "ABCB"))
