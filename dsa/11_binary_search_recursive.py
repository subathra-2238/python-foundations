# DSA-11: Binary Search using Recursion

def binary_search(numbers, target, left, right):

    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    elif numbers[middle] < target:
        return binary_search(numbers, target, middle + 1, right)

    else:
        return binary_search(numbers, target, left, middle - 1)


numbers = [10, 20, 30, 40, 50, 60, 70]

target = 60

result = binary_search(numbers, target, 0, len(numbers) - 1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
    