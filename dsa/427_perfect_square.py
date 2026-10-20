def is_perfect_square(n):
    if n < 0:
        return False

    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1

    return False


print("25:", is_perfect_square(25))
print("26:", is_perfect_square(26))
print("0:", is_perfect_square(0))
print("Negative:", is_perfect_square(-4))
