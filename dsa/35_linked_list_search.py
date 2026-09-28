# DSA-35: Linked List - Search


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


# Value to search
target = 30

current = node1
position = 0

found = False

while current is not None:

    if current.data == target:
        print("Element found at position:", position)
        found = True
        break

    current = current.next
    position += 1


if not found:
    print("Element not found")