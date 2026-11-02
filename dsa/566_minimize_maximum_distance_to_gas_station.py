
def can_place(stations, k, max_distance):
    needed = 0

    for i in range(1, len(stations)):
        distance = stations[i] - stations[i - 1]

        # Number of new stations needed in this gap
        needed += int(distance / max_distance)

        # Avoid adding one when the gap is an exact multiple
        if distance % max_distance == 0:
            needed -= 1

        if needed > k:
            return False

    return True


def minimize_max_distance(stations, k):
    low = 0.0
    high = max(
        stations[i] - stations[i - 1]
        for i in range(1, len(stations))
    )

    answer = high

    while high - low > 1e-6:
        mid = (low + high) / 2

        if can_place(stations, k, mid):
            answer = mid
            high = mid
        else:
            low = mid

    return round(answer, 6)


stations = [1, 10]
k = 1

print("Minimum maximum distance:",
      minimize_max_distance(stations, k))
