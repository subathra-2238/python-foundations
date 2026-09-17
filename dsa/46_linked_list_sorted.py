# DSA-46: Linked List - Check if Sorted


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


# Check if sorted
current = node1
is_sorted = True

while current.next is not None:

    if current.data > current.next.data:
        is_sorted = False
        break

    current = current.next


if is_sorted:
    print("Linked list is sorted")
else:
    print("Linked list is not sorted")