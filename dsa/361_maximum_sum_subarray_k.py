
def max_subarray_sum(arr, k):
    if k <= 0 or k > len(arr):
        return None

    window_sum = sum(arr[:k])
    maximum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        maximum = max(maximum, window_sum)

    return maximum


numbers = [2, 1, 5, 1, 3, 2]
k = 3

print("Maximum subarray sum:", max_subarray_sum(numbers, k))
