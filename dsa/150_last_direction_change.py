class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def last_direction_change(head):
    if head is None or head.next is None or head.next.next is None:
        return None

    previous = head
    current = head.next
    result = None

    if current.data > previous.data:
        direction = 1
    elif current.data < previous.data:
        direction = -1
    else:
        direction = 0

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
            result = next_node.data

        direction = new_direction
        previous = current
        current = next_node

    return result


# Create linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(14)
head.next.next.next.next.next.next = Node(18)
head.next.next.next.next.next.next.next = Node(10)

result = last_direction_change(head)

print("Last direction change:", result)