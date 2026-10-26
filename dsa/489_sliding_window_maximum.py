
from collections import deque


def sliding_window_maximum(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return []

    window = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices outside the current window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove smaller elements from the back
        while window and nums[window[-1]] <= nums[i]:
            window.pop()

        window.append(i)

        # Record the maximum once the first window is complete
        if i >= k - 1:
            result.append(nums[window[0]])

    return result


print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sliding_window_maximum([1, -1], 1))
print(sliding_window_maximum([4, 2, 7], 2))
