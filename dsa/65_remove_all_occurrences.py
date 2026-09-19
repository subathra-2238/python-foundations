class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)

head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(2)


def remove_all(head, value):
    while head is not None and head.data == value:
        head = head.next

    current = head

    while current is not None and current.next is not None:
        if current.next.data == value:
            current.next = current.next.next
        else:
            current = current.next

    return head


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Original linked list:")
display(head)

head = remove_all(head, 2)

print("After removing all 2s:")
display(head)