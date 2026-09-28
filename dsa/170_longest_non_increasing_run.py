class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_non_increasing_run(head):
    if head is None:
        return 0

    current = head

    current_length = 1
    longest_length = 1

    while current is not None and current.next is not None:

        if current.data >= current.next.data:
            current_length += 1

            if current_length > longest_length:
                longest_length = current_length
        else:
            current_length = 1

        current = current.next

    return longest_length


# Create linked list
head = Node(20)
head.next = Node(15)
head.next.next = Node(15)
head.next.next.next = Node(10)
head.next.next.next.next = Node(18)
head.next.next.next.next.next = Node(12)
head.next.next.next.next.next.next = Node(12)
head.next.next.next.next.next.next.next = Node(20)

result = longest_non_increasing_run(head)

print("Length of longest non-increasing run:", result)