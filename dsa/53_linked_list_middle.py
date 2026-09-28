# DSA-53: Linked List - Find Middle Element


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Find middle using slow and fast pointers
slow = node1
fast = node1

while fast is not None and fast.next is not None:

    slow = slow.next
    fast = fast.next.next


print("Middle element:", slow.data)