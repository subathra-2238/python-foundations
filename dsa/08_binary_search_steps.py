# DSA-08: Binary Search Steps

numbers = [10, 20, 30, 40, 50, 60, 70]

target = 60

left = 0
right = len(numbers) - 1

while left <= right:

    middle = (left + right) // 2

    print("Left:", left, "Middle:", middle, "Right:", right)

    if numbers[middle] == target:
        print("Found:", numbers[middle])
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1