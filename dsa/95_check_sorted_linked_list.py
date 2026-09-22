class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def is_sorted(head):
    if head is None or head.next is None:
        return True

    current = head

    while current.next is not None:

        if current.data > current.next.data:
            return False

        current = current.next

    return True


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

if is_sorted(head):
    print("The linked list is sorted.")
else:
    print("The linked list is not sorted.")