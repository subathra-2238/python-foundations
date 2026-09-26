class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_alternating_runs(head):
    if head is None or head.next is None:
        return 0

    previous = head
    current = head.next

    direction = 0
    runs = 1

    while current.next is not None:
        next_node = current.next

        if current.data > previous.data:
            current_direction = 1
        elif current.data < previous.data:
            current_direction = -1
        else:
            direction = 0
            previous = current
            current = next_node
            continue

        if direction != 0 and current_direction == direction:
            runs += 1

        direction = current_direction

        previous = current
        current = next_node

    return runs


# Create linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(20)
head.next.next.next.next = Node(12)
head.next.next.next.next.next = Node(18)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(7)

result = count_alternating_runs(head)

print("Alternating runs:", result)