class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(20)

head.next = Node(15)
head.next.next = Node(12)
head.next.next.next = Node(8)
head.next.next.next.next = Node(5)


def first_less_value(head, value):
    current = head

    while current is not None:

        if current.data < value:
            return current.data

        current = current.next

    return None


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

value = 10

result = first_less_value(head, value)

print("Given value:", value)

if result is not None:
    print("First value less than", value, ":", result)
else:
    print("No value less than", value)