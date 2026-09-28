class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_local_peaks(head):
    if head is None or head.next is None or head.next.next is None:
        return 0

    count = 0
    current = head.next

    while current.next is not None:
        if current.data > current.next.data and current.data > head.data:
            count += 1

        head = current
        current = current.next

    return count


# Create linked list
head = Node(5)
head.next = Node(10)
head.next.next = Node(6)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next = Node(7)

result = count_local_peaks(head)

print("Local peaks:", result)