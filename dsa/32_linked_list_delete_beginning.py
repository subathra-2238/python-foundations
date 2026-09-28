# DSA-32: Linked List - Delete from Beginning


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


# Delete first node
node1 = node1.next


# Traverse
current = node1

while current is not None:
    print(current.data)
    current = current.next