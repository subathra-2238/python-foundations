
def can_place_cows(stalls, k, distance):
    cows_placed = 1
    last_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= distance:
            cows_placed += 1
            last_position = stalls[i]

        if cows_placed >= k:
            return True

    return False


def aggressive_cows(stalls, k):
    if k < 1 or k > len(stalls):
        return -1

    stalls.sort()

    if k == 1:
        return 0

    left = 1
    right = stalls[-1] - stalls[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place_cows(stalls, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(aggressive_cows([1, 2, 8, 4, 9], 3))
print(aggressive_cows([10, 1, 2, 7, 5], 3))
print(aggressive_cows([1, 2, 3, 4], 2))
print(aggressive_cows([5, 10, 15], 1))
