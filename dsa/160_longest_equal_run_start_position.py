class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_equal_run_start_position(head):
    if head is None:
        return -1

    current = head
    current_start = 1
    current_length = 1

    best_start = 1
    best_length = 1

    position = 1

    while current.next is not None:
        position += 1

        if current.next.data == current.data:
            current_length += 1
        else:
            if current_length > best_length:
                best_length = current_length
                best_start = current_start

            current_start = position
            current_length = 1

        current = current.next

    if current_length > best_length:
        best_start = current_start

    return best_start


# Create linked list
head = Node(5)
head.next = Node(5)
head.next.next = Node(8)
head.next.next.next = Node(8)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next.next.next.next = Node(10)

result = longest_equal_run_start_position(head)

print("Start position of longest equal run:", result)
# DSA-160: Find the starting position of the longest equal run.