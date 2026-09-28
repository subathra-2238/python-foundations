class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def last_peak_or_valley(head):
    if head is None or head.next is None:
        return None

    previous = head
    current = head.next
    result = None

    while current.next is not None:
        next_node = current.next

        # Local peak or local valley
        if ((current.data > previous.data and current.data > next_node.data) or
                (current.data < previous.data and current.data < next_node.data)):
            result = current.data

        previous = current
        current = next_node

    return result


# Create linked list
head = Node(10)
head.next = Node(5)
head.next.next = Node(12)
head.next.next.next = Node(6)
head.next.next.next.next = Node(15)
head.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next = Node(20)

result = last_peak_or_valley(head)

print("Last peak or valley:", result)