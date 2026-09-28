class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_equal_run(head):
    if head is None:
        return 0

    current = head
    current_length = 1
    longest = 1

    while current.next is not None:
        if current.next.data == current.data:
            current_length += 1

            if current_length > longest:
                longest = current_length
        else:
            current_length = 1

        current = current.next

    return longest


# Create linked list
head = Node(5)
head.next = Node(5)
head.next.next = Node(5)
head.next.next.next = Node(8)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next.next.next.next = Node(10)

result = longest_equal_run(head)

print("Longest equal run:", result)