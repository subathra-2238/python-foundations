class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(12)

head.next = Node(7)
head.next.next = Node(15)
head.next.next.next = Node(20)
head.next.next.next.next = Node(7)


def find_position(head, value):
    current = head
    position = 1

    while current is not None:

        if current.data == value:
            return position

        current = current.next
        position += 1

    return -1


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

value = 20

position = find_position(head, value)

print("Given value:", value)

if position != -1:
    print("Position of", value, ":", position)
else:
    print("Value not found")