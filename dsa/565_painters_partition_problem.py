
def can_paint(boards, painters, limit):
    painters_used = 1
    current_time = 0

    for board in boards:
        if board > limit:
            return False

        if current_time + board > limit:
            painters_used += 1
            current_time = board
        else:
            current_time += board

    return painters_used <= painters


def painter_partition(boards, painters):
    n = len(boards)

    if painters <= 0 or painters > n:
        return -1

    left = max(boards)
    right = sum(boards)

    while left < right:
        mid = (left + right) // 2

        if can_paint(boards, painters, mid):
            right = mid
        else:
            left = mid + 1

    return left


print(painter_partition([10, 20, 30, 40], 2))
print(painter_partition([5, 5, 5, 5], 2))
print(painter_partition([10, 20, 30], 3))
print(painter_partition([10, 20], 3))
