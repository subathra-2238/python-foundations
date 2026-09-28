# DSA-10: Linear Search vs Binary Search

numbers = [10, 20, 30, 40, 50, 60, 70]

target = 60


# Linear Search
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Linear Search: Found at index", i)
        break


# Binary Search
left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Binary Search: Found at index", middle)
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1