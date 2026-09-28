# DSA-05: Linear Search using a Function

def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1


numbers = [10, 25, 37, 42, 56, 68]

target = 42

result = linear_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")