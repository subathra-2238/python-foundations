# DSA-59: Linked List - Palindrome using Two Pointers


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


# Find middle
slow = node1
fast = node1

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next


# Reverse second half
previous = None
current = slow

while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node


# Compare first half and reversed second half
first = node1
second = previous

is_palindrome = True

while second is not None:

    if first.data != second.data:
        is_palindrome = False
        break

    first = first.next
    second = second.next


if is_palindrome:
    print("Linked list is a palindrome")
else:
    print("Linked list is not a palindrome")