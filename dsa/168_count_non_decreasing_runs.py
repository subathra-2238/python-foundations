class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_non_decreasing_runs(head):
    if head is None:
        return 0

    current = head
    count = 0

    while current is not None and current.next is not None:

        if current.data <= current.next.data:
            count += 1

            while (
                current.next is not None
                and current.data <= current.next.data
            ):
                current = current.next

        current = current.next

    return count


# Create linked list
head = Node(5)
head.next = Node(10)
head.next.next = Node(10)
head.next.next.next = Node(15)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(12)
head.next.next.next.next.next.next = Node(12)
head.next.next.next.next.next.next.next = Node(20)
head.next.next.next.next.next.next.next.next = Node(18)

result = count_non_decreasing_runs(head)

print("Number of non-decreasing runs:", result)