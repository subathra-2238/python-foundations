class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)

head.next = Node(3)
head.next.next = Node(5)
head.next.next.next = Node(7)


def delete_node(head, value):
    if head is None:
        return None

    if head.data == value:
        return head.next

    current = head

    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next
            return head

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

head = delete_node(head, 5)

print("After deleting 5:")
display(head)