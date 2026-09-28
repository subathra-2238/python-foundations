class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_peaks_and_valleys(head):
    if head is None or head.next is None:
        return 0

    previous = head
    current = head.next
    count = 0

    while current.next is not None:
        next_node = current.next

        # Local peak
        if current.data > previous.data and current.data > next_node.data:
            count += 1

        # Local valley
        elif current.data < previous.data and current.data < next_node.data:
            count += 1

        previous = current
        current = next_node

    return count


# Create linked list
head = Node(5)
head.next = Node(10)
head.next.next = Node(6)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next = Node(7)

result = count_peaks_and_valleys(head)

print("Total peaks and valleys:", result)