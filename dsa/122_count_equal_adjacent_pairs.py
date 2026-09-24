class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_equal_adjacent_pairs(head):
    if head is None or head.next is None:
        return 0

    count = 0
    current = head

    while current.next is not None:
        if current.next.data == current.data:
            count += 1

        current = current.next

    return count


# Create linked list
head = Node(10)
head.next = Node(10)
head.next.next = Node(5)
head.next.next.next = Node(8)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next = Node(12)

result = count_equal_adjacent_pairs(head)

print("Equal adjacent pairs:", result)