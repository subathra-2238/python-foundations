# DSA-37: Linked List - Reverse


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


# Reverse the linked list
previous = None
current = node1

while current is not None:

    next_node = current.next

    current.next = previous

    previous = current
    current = next_node


# New head
node1 = previous


# Traverse reversed list
current = node1

while current is not None:
    print(current.data)
    current = current.next