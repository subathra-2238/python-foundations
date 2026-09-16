# DSA-33: Linked List - Delete from End


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3


# Find the second-last node
current = node1

while current.next.next is not None:
    current = current.next


# Delete the last node
current.next = None


# Traverse
current = node1

while current is not None:
    print(current.data)
    current = current.next