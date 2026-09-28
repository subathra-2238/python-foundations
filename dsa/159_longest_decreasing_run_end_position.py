class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_decreasing_run_end_position(head):
    if head is None:
        return -1

    if head.next is None:
        return 1

    current = head
    current_length = 1

    best_length = 1
    best_end = 1

    position = 1

    while current.next is not None:
        position += 1

        if current.next.data < current.data:
            current_length += 1
        else:
            if current_length > best_length:
                best_length = current_length
                best_end = position - 1

            current_length = 1

        current = current.next

    if current_length > best_length:
        best_end = position

    return best_end


# Create linked list
head = Node(30)
head.next = Node(25)
head.next.next = Node(20)
head.next.next.next = Node(28)
head.next.next.next.next = Node(15)
head.next.next.next.next.next = Node(10)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(12)

result = longest_decreasing_run_end_position(head)

print("End position of longest decreasing run:", result)