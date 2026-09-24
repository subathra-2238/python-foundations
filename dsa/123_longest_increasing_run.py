class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_increasing_run(head):
    if head is None:
        return 0

    current = head
    current_length = 1
    longest = 1

    while current.next is not None:
        if current.next.data > current.data:
            current_length += 1

            if current_length > longest:
                longest = current_length
        else:
            current_length = 1

        current = current.next

    return longest


# Create linked list
head = Node(10)
head.next = Node(12)
head.next.next = Node(15)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(11)
head.next.next.next.next.next.next = Node(5)

result = longest_increasing_run(head)

print("Longest increasing run:", result)