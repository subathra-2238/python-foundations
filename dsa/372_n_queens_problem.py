
def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            safe = True

            for previous_row in range(row):
                previous_col = board[previous_row]

                if previous_col == col or abs(previous_col - col) == abs(previous_row - row):
                    safe = False
                    break

            if safe:
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


n = 4
solutions = solve_n_queens(n)

print("Board size:", n)
print("Number of solutions:", len(solutions))

for solution in solutions:
    for col in solution:
        print("." * col + "Q" + "." * (n - col - 1))
    print()
