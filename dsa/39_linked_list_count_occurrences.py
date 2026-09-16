# DSA-39: Linked List - Count Occurrences


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(10)
node4 = Node(30)
node5 = Node(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Value to count
target = 10

current = node1
count = 0

while current is not None:

    if current.data == target:
        count += 1

    current = current.next


print("Occurrences of", target, ":", count)