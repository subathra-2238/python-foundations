# DSA-42: Linked List - Find Sum


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


# Find sum
current = node1
total = 0

while current is not None:

    total += current.data

    current = current.next


print("Sum of elements:", total)