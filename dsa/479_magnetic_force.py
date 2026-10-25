
def max_min_distance(position, m):
    position.sort()

    left = 1
    right = position[-1] - position[0]

    while left <= right:
        distance = (left + right) // 2
        balls = 1
        last_position = position[0]

        for i in range(1, len(position)):
            if position[i] - last_position >= distance:
                balls += 1
                last_position = position[i]

        if balls >= m:
            left = distance + 1
        else:
            right = distance - 1

    return right


print(max_min_distance([1, 2, 3, 4, 7], 3))
print(max_min_distance([5, 4, 3, 2, 1, 1000000000], 2))
print(max_min_distance([1, 2], 2))
