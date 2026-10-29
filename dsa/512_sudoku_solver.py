
def solve_sudoku(board):
    def is_valid(row, col, num):
        # Check the row and column
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False

        # Find the top-left corner of the 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in "123456789":
                        if is_valid(row, col, num):
                            board[row][col] = num

                            if backtrack():
                                return True

                            # Undo the incorrect choice
                            board[row][col] = "."

                    return False

        return True

    return backtrack()


board = [
    list("53..7...."),
    list("6..195..."),
    list(".98....6."),
    list("8...6...3"),
    list("4..8.3..1"),
    list("7...2...6"),
    list(".6....28."),
    list("...419..5"),
    list("....8..79")
]

if solve_sudoku(board):
    for row in board:
        print(" ".join(row))
else:
    print("No solution exists.")
