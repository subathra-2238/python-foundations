
import heapq


def last_stone_weight(stones):
    # Convert weights into a max-heap using negative values
    stones = [-stone for stone in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        heaviest = -heapq.heappop(stones)
        second = -heapq.heappop(stones)

        if heaviest != second:
            remaining = heaviest - second
            heapq.heappush(stones, -remaining)

    return -stones[0] if stones else 0


print(last_stone_weight([2, 7, 4, 1, 8, 1]))
print(last_stone_weight([1]))
print(last_stone_weight([3, 3]))
