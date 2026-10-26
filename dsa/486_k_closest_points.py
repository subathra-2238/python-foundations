
import heapq


def k_closest(points, k):
    heap = []

    for x, y in points:
        distance = x * x + y * y
        heapq.heappush(heap, (distance, x, y))

    result = []

    for _ in range(k):
        distance, x, y = heapq.heappop(heap)
        result.append([x, y])

    return result


print(k_closest([[1, 3], [-2, 2], [5, 8], [0, 1]], 2))
print(k_closest([[3, 3], [5, -1], [-2, 4]], 1))
