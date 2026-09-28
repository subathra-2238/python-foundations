class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_local_valleys(head):
    if head is None or head.next is None or head.next.next is None:
        return 0

    count = 0
    previous = head
    current = head.next

    while current.next is not None:
        if current.data < previous.data and current.data < current.next.data:
            count += 1

        previous = current
        current = current.next

    return count


# Create linked list
head = Node(10)
head.next = Node(5)
head.next.next = Node(12)
head.next.next.next = Node(6)
head.next.next.next.next = Node(15)
head.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next = Node(20)

result = count_local_valleys(head)

print("Local valleys:", result)