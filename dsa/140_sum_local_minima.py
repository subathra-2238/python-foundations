class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sum_local_minima(head):
    if head is None or head.next is None:
        return 0

    previous = head
    current = head.next
    total = 0

    while current.next is not None:
        next_node = current.next

        if current.data < previous.data and current.data < next_node.data:
            total += current.data

        previous = current
        current = next_node

    return total


# Create linked list
head = Node(10)
head.next = Node(5)
head.next.next = Node(12)
head.next.next.next = Node(6)
head.next.next.next.next = Node(15)
head.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next = Node(20)

result = sum_local_minima(head)

print("Sum of local minima:", result)