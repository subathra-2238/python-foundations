class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(-5)
head.next.next = Node(20)
head.next.next.next = Node(15)
head.next.next.next.next = Node(3)


def count_greater_than(head, value):
    count = 0

    current = head

    while current is not None:

        if current.data > value:
            count += 1

        current = current.next

    return count


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

value = 10

count = count_greater_than(head, value)

print("Given value:", value)
print("Values greater than", value, ":", count)