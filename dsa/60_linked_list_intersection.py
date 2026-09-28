# DSA-60: Linked List - Find Intersection Point


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# First list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3


# Second list
node4 = Node(5)
node5 = Node(15)

node4.next = node5
node5.next = node2


# Find intersection
first = node1
second = node4

while first != second:

    if first is None:
        first = node4
    else:
        first = first.next

    if second is None:
        second = node1
    else:
        second = second.next


print("Intersection point:", first.data)