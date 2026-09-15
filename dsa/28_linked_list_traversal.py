# DSA-28: Linked List Traversal


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


# Traversal
current = node1

while current is not None:
    print("Data:", current.data)
    current = current.next