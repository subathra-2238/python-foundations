
import heapq


def merge_k_sorted_lists(lists):
    min_heap = []

    # Add the first element of each non-empty list
    for i, arr in enumerate(lists):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    result = []

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        next_index = element_index + 1
        arr = lists[list_index]

        if next_index < len(arr):
            heapq.heappush(
                min_heap,
                (arr[next_index], list_index, next_index)
            )

    return result


print(merge_k_sorted_lists([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
print(merge_k_sorted_lists([[1, 3], [2, 4], [0, 5]]))
print(merge_k_sorted_lists([[], [1, 2], []]))
