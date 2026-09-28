class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)
head.next.next.next.next.next = Node(30)
head.next.next.next.next.next.next = Node(40)


def remove_duplicates(head):
    current = head

    while current is not None and current.next is not None:

        if current.data == current.next.data:
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

head = remove_duplicates(head)

print("After removing duplicates:")
display(head)