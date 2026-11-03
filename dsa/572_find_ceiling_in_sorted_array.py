
def find_ceiling(arr, target):
    low = 0
    high = len(arr) - 1

    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]

        elif arr[mid] > target:
            answer = arr[mid]
            high = mid - 1

        else:
            low = mid + 1

    return answer


arr = [1, 2, 4, 6, 10, 12, 14]
target = 7

print("Ceiling:", find_ceiling(arr, target))
