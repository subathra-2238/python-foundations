class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_increasing_decreasing_runs(head):
    if head is None or head.next is None:
        return 0, 0

    previous = head
    current = head.next

    increasing_runs = 0
    decreasing_runs = 0
    direction = 0

    while current is not None:
        if current.data > previous.data:
            new_direction = 1
        elif current.data < previous.data:
            new_direction = -1
        else:
            direction = 0
            previous = current
            current = current.next
            continue

        if new_direction != direction:
            if new_direction == 1:
                increasing_runs += 1
            else:
                decreasing_runs += 1

            direction = new_direction

        previous = current
        current = current.next

    return increasing_runs, decreasing_runs


# Create linked list
head = Node(10)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(14)
head.next.next.next.next.next.next = Node(18)
head.next.next.next.next.next.next.next = Node(10)

inc, dec = count_increasing_decreasing_runs(head)

print("Increasing runs:", inc)
print("Decreasing runs:", dec)