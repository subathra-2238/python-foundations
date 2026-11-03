
def find_kth_missing(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        missing = arr[mid] - (mid + 1)

        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k


arr = [2, 3, 4, 7, 11]
k = 5

print("Kth missing positive number:", find_kth_missing(arr, k))
