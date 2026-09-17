# DSA-44: Linked List - Find Second Largest


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


# Find largest and second largest
current = node1

largest = float("-inf")
second_largest = float("-inf")

while current is not None:

    if current.data > largest:
        second_largest = largest
        largest = current.data

    elif current.data > second_largest and current.data != largest:
        second_largest = current.data

    current = current.next


print("Largest element:", largest)
print("Second largest element:", second_largest)