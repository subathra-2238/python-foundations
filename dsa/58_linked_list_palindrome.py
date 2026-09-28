# DSA-58: Linked List - Check Palindrome


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(20)
node5 = Node(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Store elements in a list
values = []

current = node1

while current is not None:
    values.append(current.data)
    current = current.next


# Check palindrome
if values == values[::-1]:
    print("Linked list is a palindrome")
else:
    print("Linked list is not a palindrome")