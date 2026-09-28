class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)

head.next = Node(3)
head.next.next = Node(5)
head.next.next.next = Node(7)


def insert_sorted(head, value):
    new_node = Node(value)

    if head is None or value < head.data:
        new_node.next = head
        return new_node

    current = head

    while current.next is not None and current.next.data < value:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Original linked list:")
display(head)

head = insert_sorted(head, 4)

print("After inserting 4:")
display(head)