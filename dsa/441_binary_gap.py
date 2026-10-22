def binary_gap(n):
    last_position = -1
    longest = 0
    position = 0

    while n > 0:
        if n & 1:
            if last_position != -1:
                longest = max(longest, position - last_position)

            last_position = position

        n >>= 1
        position += 1

    return longest


print("22:", binary_gap(22))
print("8:", binary_gap(8))
print("5:", binary_gap(5))
print("6:", binary_gap(6))
