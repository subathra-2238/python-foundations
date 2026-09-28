# DSA-36: Linked List - Find Length


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


# Find length
current = node1
length = 0

while current is not None:
    length += 1
    current = current.next


print("Length of linked list:", length)