# DSA-41: Linked List - Find Minimum


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(25)
node2 = Node(10)
node3 = Node(45)
node4 = Node(30)

node1.next = node2
node2.next = node3
node3.next = node4


# Find minimum
current = node1
minimum = node1.data

while current is not None:

    if current.data < minimum:
        minimum = current.data

    current = current.next


print("Minimum element:", minimum)