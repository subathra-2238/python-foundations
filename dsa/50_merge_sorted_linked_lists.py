# DSA-50: Merge Two Sorted Linked Lists


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# First sorted linked list
node1 = Node(10)
node2 = Node(30)
node3 = Node(50)

node1.next = node2
node2.next = node3


# Second sorted linked list
node4 = Node(20)
node5 = Node(40)
node6 = Node(60)

node4.next = node5
node5.next = node6


# Merge the two lists
list1 = node1
list2 = node4

dummy = Node(0)
current = dummy

while list1 is not None and list2 is not None:

    if list1.data < list2.data:
        current.next = list1
        list1 = list1.next

    else:
        current.next = list2
        list2 = list2.next

    current = current.next


# Add remaining nodes
if list1 is not None:
    current.next = list1

if list2 is not None:
    current.next = list2


# New head
merged_head = dummy.next


# Display merged list
current = merged_head

while current is not None:
    print(current.data)
    current = current.next