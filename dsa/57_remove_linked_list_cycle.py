# DSA-57: Linked List - Remove Cycle


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Create cycle
node5.next = node3


# Detect cycle
slow = node1
fast = node1

cycle_found = False

while fast is not None and fast.next is not None:

    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle_found = True
        break


# Remove cycle
if cycle_found:

    slow = node1

    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Find the last node in the cycle
    cycle_last = slow

    while cycle_last.next != slow:
        cycle_last = cycle_last.next

    cycle_last.next = None


# Display linked list
current = node1

while current is not None:
    print(current.data)
    current = current.next