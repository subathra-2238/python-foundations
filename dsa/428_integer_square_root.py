def integer_sqrt(n):
    if n < 2:
        return n

    left = 1
    right = n // 2
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print("Square root of 25:", integer_sqrt(25))
print("Square root of 26:", integer_sqrt(26))
print("Square root of 100:", integer_sqrt(100))
