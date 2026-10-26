
import heapq


class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap for the smaller half
        self.large = []  # Min-heap for the larger half

    def add_num(self, num):
        # Add to the max-heap using negative values
        heapq.heappush(self.small, -num)

        # Move the largest of the smaller half to the larger half
        largest_small = -heapq.heappop(self.small)
        heapq.heappush(self.large, largest_small)

        # Keep the smaller half at least as large as the larger half
        if len(self.small) < len(self.large):
            smallest_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -smallest_large)

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2


finder = MedianFinder()

finder.add_num(1)
print(finder.find_median())

finder.add_num(2)
print(finder.find_median())

finder.add_num(3)
print(finder.find_median())

finder.add_num(4)
print(finder.find_median())
