class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def longest_alternating_run(head):
    if head is None:
        return 0

    if head.next is None:
        return 1

    previous = head
    current = head.next

    current_length = 2
    maximum_length = 1
    previous_direction = 0

    while current.next is not None:
        next_node = current.next

        if current.data > previous.data:
            direction = 1
        elif current.data < previous.data:
            direction = -1
        else:
            current_length = 1
            previous_direction = 0
            previous = current
            current = next_node
            continue

        if previous_direction != 0 and direction != previous_direction:
            current_length += 1
        else:
            current_length = 2

        maximum_length = max(maximum_length, current_length)

        previous_direction = direction
        previous = current
        current = next_node

    return maximum_length


# Create linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(20)
head.next.next.next.next = Node(12)
head.next.next.next.next.next = Node(18)
head.next.next.next.next.next.next = Node(5)

result = longest_alternating_run(head)

print("Longest alternating run:", result)