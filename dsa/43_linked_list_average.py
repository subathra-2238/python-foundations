# DSA-43: Linked List - Find Average


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


# Find sum and count
current = node1
total = 0
count = 0

while current is not None:

    total += current.data
    count += 1

    current = current.next


# Calculate average
average = total / count

print("Average:", average)