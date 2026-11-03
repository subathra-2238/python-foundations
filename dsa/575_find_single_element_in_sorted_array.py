
def find_single_element(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        # Make mid an even index
        if mid % 2 == 1:
            mid -= 1

        # Check whether the pair is correct
        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return arr[low]


arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]

print("Single element:", find_single_element(arr))
