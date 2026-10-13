
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


numbers = [1, 3, 5, 2, 2]
print("Equilibrium index:", equilibrium_index(numbers))
