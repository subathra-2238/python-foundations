# DSA-34: Linked List - Delete at a Given Position


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4


# Delete node at position 2
position = 2

current = node1

# Move to the node before the target
for _ in range(position - 1):
    current = current.next


# Skip the target node
current.next = current.next.next


# Traverse
current = node1

while current is not None:
    print(current.data)
    current = current.next