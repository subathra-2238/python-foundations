class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def delete_value(head, value):
    # Empty list
    if head is None:
        return None

    # Delete head
    if head.data == value:
        return head.next

    current = head

    # Find the node before the target
    while current.next is not None:

        if current.next.data == value:
            current.next = current.next.next
            return head

        # Since the list is sorted
        if current.next.data > value:
            break

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

value = 30
head = delete_value(head, value)

print("After deleting", value, ":")
display(head)