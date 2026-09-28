class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_direction_changes_by_type(head):
    if head is None or head.next is None:
        return 0, 0

    previous = head
    current = head.next

    increasing_to_decreasing = 0
    decreasing_to_increasing = 0

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

        if direction == 1 and new_direction == -1:
            increasing_to_decreasing += 1
        elif direction == -1 and new_direction == 1:
            decreasing_to_increasing += 1

        direction = new_direction

        previous = current
        current = next_node

    return increasing_to_decreasing, decreasing_to_increasing


# Create linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(14)
head.next.next.next.next.next.next = Node(18)
head.next.next.next.next.next.next.next = Node(10)

inc_dec, dec_inc = count_direction_changes_by_type(head)

print("Increasing to decreasing:", inc_dec)
print("Decreasing to increasing:", dec_inc)