
def find_floor(arr, target):
    low = 0
    high = len(arr) - 1

    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return arr[mid]

        elif arr[mid] < target:
            answer = arr[mid]
            low = mid + 1

        else:
            high = mid - 1

    return answer


arr = [1, 2, 4, 6, 10, 12, 14]
target = 7

print("Floor:", find_floor(arr, target))
