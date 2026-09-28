class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def first_direction_change_position(head):
    if head is None or head.next is None or head.next.next is None:
        return -1

    previous = head
    current = head.next
    position = 2

    if current.data > previous.data:
        direction = 1
    elif current.data < previous.data:
        direction = -1
    else:
        direction = 0

    while current.next is not None:
        next_node = current.next
        position += 1

        if current.data < next_node.data:
            new_direction = 1
        elif current.data > next_node.data:
            new_direction = -1
        else:
            previous = current
            current = next_node
            continue

        if direction != 0 and new_direction != direction:
            return position

        direction = new_direction
        previous = current
        current = next_node

    return -1


# Create linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(14)

result = first_direction_change_position(head)

print("First direction change position:", result)