class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_direction_changes_at_nodes(head):
    if head is None or head.next is None or head.next.next is None:
        return 0

    previous = head
    current = head.next

    if current.data > previous.data:
        direction = 1
    elif current.data < previous.data:
        direction = -1
    else:
        direction = 0

    count = 0

    while current.next is not None:
        next_node = current.next

        if current.data < next_node.data:
            new_direction = 1
        elif current.data > next_node.data:
            new_direction = -1
        else:
            previous = current
            current = next_node
            continue

        if direction != 0 and new_direction != direction:
            count += 1

        direction = new_direction
        previous = current
        current = next_node

    return count


# Create linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(14)
head.next.next.next.next.next.next = Node(18)
head.next.next.next.next.next.next.next = Node(10)

result = count_direction_changes_at_nodes(head)

print("Direction changes:", result)