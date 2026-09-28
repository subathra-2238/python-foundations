class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(12)

head.next = Node(7)
head.next.next = Node(15)
head.next.next.next = Node(7)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(7)


def last_equal_value(head, value):
    current = head
    result = None

    while current is not None:

        if current.data == value:
            result = current.data

        current = current.next

    return result


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

value = 7

result = last_equal_value(head, value)

print("Given value:", value)

if result is not None:
    print("Last value equal to", value, ":", result)
else:
    print("Value not found")