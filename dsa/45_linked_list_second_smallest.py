# DSA-45: Linked List - Find Second Smallest


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(50)
node3 = Node(30)
node4 = Node(40)
node5 = Node(20)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Find smallest and second smallest
current = node1

smallest = float("inf")
second_smallest = float("inf")

while current is not None:

    if current.data < smallest:
        second_smallest = smallest
        smallest = current.data

    elif current.data < second_smallest and current.data != smallest:
        second_smallest = current.data

    current = current.next


print("Smallest element:", smallest)
print("Second smallest element:", second_smallest)