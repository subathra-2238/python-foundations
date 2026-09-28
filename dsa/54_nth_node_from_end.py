# DSA-54: Linked List - Find Nth Node from End


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


# Find 2nd node from the end
n = 2

slow = node1
fast = node1


# Move fast pointer n steps
for _ in range(n):
    fast = fast.next


# Move both pointers
while fast is not None:
    slow = slow.next
    fast = fast.next


print("Nth node from end:", slow.data)