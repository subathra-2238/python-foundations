class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def maximum_local_maximum(head):
    if head is None or head.next is None:
        return None

    previous = head
    current = head.next
    maximum = None

    while current.next is not None:
        next_node = current.next

        if current.data > previous.data and current.data > next_node.data:
            if maximum is None or current.data > maximum:
                maximum = current.data

        previous = current
        current = next_node

    return maximum


# Create linked list
head = Node(5)
head.next = Node(10)
head.next.next = Node(6)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next = Node(7)

result = maximum_local_maximum(head)

print("Maximum local maximum:", result)