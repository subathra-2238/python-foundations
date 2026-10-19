
from collections import Counter
import heapq


def reorganize_string(s):
    counts = Counter(s)
    heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(heap)

    result = []
    previous_count = 0
    previous_char = ""

    while heap:
        count, char = heapq.heappop(heap)
        result.append(char)

        if previous_count < 0:
            heapq.heappush(heap, (previous_count, previous_char))

        count += 1
        previous_count = count
        previous_char = char

    answer = "".join(result)

    for i in range(1, len(answer)):
        if answer[i] == answer[i - 1]:
            return ""

    return answer


text = "aaabbc"
result = reorganize_string(text)

if result:
    print("Reorganized string:", result)
else:
    print("Reorganization is impossible")
