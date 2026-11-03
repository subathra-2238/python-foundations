
def find_minimum(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            # Minimum is in the right half
            low = mid + 1

        else:
            # Minimum is at mid or in the left half
            high = mid

    return arr[low]


arr = [4, 5, 6, 7, 0, 1, 2]

print("Minimum element:", find_minimum(arr))
