class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_equal_runs(head):
    if head is None:
        return 0

    current = head
    count = 0

    while current is not None and current.next is not None:

        if current.data == current.next.data:
            count += 1

            # Move to the end of the equal run
            while (
                current.next is not None
                and current.data == current.next.data
            ):
                current = current.next

        current = current.next

    return count


# Create linked list
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)
head.next.next.next = Node(20)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next = Node(8)

result = count_equal_runs(head)

print("Number of equal runs:", result)