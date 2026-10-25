
def ship_within_days(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        capacity = (left + right) // 2
        days_needed = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                days_needed += 1
                current_load = 0

            current_load += weight

        if days_needed <= days:
            right = capacity
        else:
            left = capacity + 1

    return left


print(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(ship_within_days([3, 2, 2, 4, 1, 4], 3))
print(ship_within_days([1, 2, 3, 1, 1], 4))
