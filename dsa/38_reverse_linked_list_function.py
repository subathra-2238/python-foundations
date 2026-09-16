# DSA-38: Linked List - Reverse using a Function


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):

    previous = None
    current = head

    while current is not None:

        next_node = current.next

        current.next = previous

        previous = current
        current = next_node

    return previous


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4


# Reverse
node1 = reverse_linked_list(node1)


# Traverse
current = node1

while current is not None:
    print(current.data)
    current = current.next