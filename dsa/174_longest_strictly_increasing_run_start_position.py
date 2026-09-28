class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_strictly_increasing_run_start_position(head):
    if head is None:
        return -1

    current = head
    position = 1

    current_length = 1
    longest_length = 1
    longest_start_position = 1
    current_start_position = 1

    while current is not None and current.next is not None:

        if current.data < current.next.data:
            current_length += 1
        else:
            current_length = 1
            current_start_position = position + 1

        if current_length > longest_length:
            longest_length = current_length
            longest_start_position = current_start_position

        current = current.next
        position += 1

    return longest_start_position


# Create linked list
head = Node(5)
head.next = Node(10)
head.next.next = Node(15)
head.next.next.next = Node(8)
head.next.next.next.next = Node(12)
head.next.next.next.next.next = Node(20)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(9)

result = longest_strictly_increasing_run_start_position(head)

print("Start position of longest strictly increasing run:", result)