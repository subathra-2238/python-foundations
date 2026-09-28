class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(25)
head.next.next = Node(7)
head.next.next.next = Node(40)
head.next.next.next.next = Node(15)


def find_maximum(head):
    if head is None:
        return None

    maximum = head.data
    current = head.next

    while current is not None:

        if current.data > maximum:
            maximum = current.data

        current = current.next

    return maximum


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

maximum = find_maximum(head)

print("Maximum value:", maximum)