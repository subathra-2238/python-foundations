# DSA-55: Linked List - Detect Cycle


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create a cycle
node4.next = node2


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


if cycle_found:
    print("Cycle detected")
else:
    print("No cycle")