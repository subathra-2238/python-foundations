
from collections import Counter


def least_interval(tasks, n):
    counts = Counter(tasks).values()
    max_count = max(counts)
    max_tasks = sum(
        count == max_count for count in counts
    )

    intervals = (max_count - 1) * (n + 1) + max_tasks

    return max(len(tasks), intervals)


print(least_interval(["A", "A", "A", "B", "B", "B"], 2))
print(least_interval(["A", "A", "A", "B", "B", "B"], 0))
print(least_interval(["A", "A", "A", "B", "B", "B"], 3))
