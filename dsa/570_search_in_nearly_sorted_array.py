
def search_nearly_sorted(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check the middle element
        if arr[mid] == target:
            return mid

        # Check the previous element
        if mid > low and arr[mid - 1] == target:
            return mid - 1

        # Check the next element
        if mid < high and arr[mid + 1] == target:
            return mid + 1

        # Eliminate the left side
        if arr[mid] > target:
            high = mid - 2

        # Eliminate the right side
        else:
            low = mid + 2

    return -1


arr = [10, 3, 40, 20, 50, 80, 70]
target = 40

print("Element index:", search_nearly_sorted(arr, target))
