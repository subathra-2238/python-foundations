class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_direction_changes(head):
    if head is None or head.next is None:
        return 0

    previous = head
    current = head.next

    direction = 0
    changes = 0

    while current.next is not None:
        next_node = current.next

        if current.data > previous.data:
            current_direction = 1
        elif current.data < previous.data:
            current_direction = -1
        else:
            previous = current
            current = next_node
            continue

        if direction != 0 and current_direction != direction:
            changes += 1

        direction = current_direction

        previous = current
        current = next_node

    return changes


# Create linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(14)
head.next.next.next.next.next.next = Node(18)
head.next.next.next.next.next.next.next = Node(10)

result = count_direction_changes(head)

print("Direction changes:", result)