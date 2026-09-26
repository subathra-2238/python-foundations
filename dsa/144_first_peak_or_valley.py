class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def first_peak_or_valley(head):
    if head is None or head.next is None:
        return None

    previous = head
    current = head.next

    while current.next is not None:
        next_node = current.next

        # Local peak
        if current.data > previous.data and current.data > next_node.data:
            return current.data

        # Local valley
        if current.data < previous.data and current.data < next_node.data:
            return current.data

        previous = current
        current = next_node

    return None


# Create linked list
head = Node(10)
head.next = Node(5)
head.next.next = Node(12)
head.next.next.next = Node(6)
head.next.next.next.next = Node(15)

result = first_peak_or_valley(head)

print("First peak or valley:", result)