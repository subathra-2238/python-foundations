
def search_rotated(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True

        # Duplicates make it impossible to identify
        # which half is sorted, so shrink both ends.
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


arr = [2, 5, 6, 0, 0, 1, 2]
target = 0

print("Target found:", search_rotated(arr, target))
