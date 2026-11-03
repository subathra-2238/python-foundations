
def find_first(arr, target):
    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            answer = mid
            high = mid - 1  # Continue searching left

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return answer


def find_last(arr, target):
    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            answer = mid
            low = mid + 1  # Continue searching right

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return answer


def search_range(arr, target):
    first = find_first(arr, target)
    last = find_last(arr, target)

    return [first, last]


arr = [1, 2, 4, 4, 4, 4, 7, 8]
target = 4

print("First and last positions:", search_range(arr, target))
