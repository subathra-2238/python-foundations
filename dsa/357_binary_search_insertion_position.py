
def search_insert_position(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


numbers = [1, 3, 5, 6]
target = 4

print("Insertion position:", search_insert_position(numbers, target))
