# DSA-51: Merge Two Unsorted Linked Lists


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# First linked list
node1 = Node(10)
node2 = Node(30)
node3 = Node(20)

node1.next = node2
node2.next = node3


# Second linked list
node4 = Node(40)
node5 = Node(15)
node6 = Node(50)

node4.next = node5
node5.next = node6


# Find the end of first list
current = node1

while current.next is not None:
    current = current.next


# Connect second list
current.next = node4


# Display merged list
current = node1

while current is not None:
    print(current.data)
    current = current.next