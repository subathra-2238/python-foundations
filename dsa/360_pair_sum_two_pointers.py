
def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1

    return False


numbers = [1, 2, 4, 6, 8, 9]
target = 10

print("Pair exists:", has_pair_with_sum(numbers, target))
