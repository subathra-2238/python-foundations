class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_equal_run_end_position(head):
    if head is None:
        return -1

    current = head
    position = 1

    best_length = 1
    best_end_position = 1

    current_length = 1
    current_end_position = 1

    while current.next is not None:
        if current.data == current.next.data:
            current_length += 1
        else:
            current_length = 1

        current_end_position = position + 1

        if current_length > best_length:
            best_length = current_length
            best_end_position = current_end_position

        current = current.next
        position += 1

    return best_end_position


# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(20)
head.next.next.next.next = Node(15)
head.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next = Node(8)

result = longest_equal_run_end_position(head)

print("End position of longest equal run:", result)