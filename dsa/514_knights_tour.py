
def knights_tour(n=5):
    board = [[-1] * n for _ in range(n)]

    # All eight possible knight moves
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    def is_safe(row, col):
        return (
            0 <= row < n
            and 0 <= col < n
            and board[row][col] == -1
        )

    def backtrack(row, col, step):
        if step == n * n:
            return True

        for dr, dc in moves:
            nr = row + dr
            nc = col + dc

            if is_safe(nr, nc):
                board[nr][nc] = step

                if backtrack(nr, nc, step + 1):
                    return True

                # Undo this move if it leads to failure
                board[nr][nc] = -1

        return False

    board[0][0] = 0

    if backtrack(0, 0, 1):
        return board

    return None


solution = knights_tour()

if solution is None:
    print("No solution found.")
else:
    for row in solution:
        print(" ".join(f"{value:2}" for value in row))
