
from collections import Counter
import heapq


def top_k_frequent(nums, k):
    frequency = Counter(nums)

    return heapq.nlargest(
        k,
        frequency.keys(),
        key=frequency.get
    )


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([1], 1))
print(top_k_frequent([4, 4, 4, 5, 5, 6], 2))
