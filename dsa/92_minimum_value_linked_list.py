class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(45)
head.next.next = Node(20)
head.next.next.next = Node(80)
head.next.next.next.next = Node(35)


def find_minimum(head):
    if head is None:
        return None

    minimum = head.data
    current = head.next

    while current is not None:
        if current.data < minimum:
            minimum = current.data

        current = current.next

    return minimum


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

result = find_minimum(head)

if result is not None:
    print("Minimum value:", result)
else:
    print("Linked list is empty.")