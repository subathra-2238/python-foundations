# DSA-47: Linked List - Count Even and Odd Elements


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(25)
node3 = Node(30)
node4 = Node(45)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Count even and odd elements
current = node1

even_count = 0
odd_count = 0

while current is not None:

    if current.data % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    current = current.next


print("Even elements:", even_count)
print("Odd elements:", odd_count)