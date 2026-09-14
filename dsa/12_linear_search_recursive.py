# DSA-12: Linear Search using Recursion

def linear_search(numbers, target, index):

    if index >= len(numbers):
        return -1

    if numbers[index] == target:
        return index

    return linear_search(numbers, target, index + 1)


numbers = [10, 25, 37, 42, 56, 68]

target = 56

result = linear_search(numbers, target, 0)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")