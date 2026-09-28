class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(-5)
head.next.next = Node(0)
head.next.next.next = Node(20)
head.next.next.next.next = Node(-15)
head.next.next.next.next.next = Node(0)


def count_values(head):
    positive = 0
    negative = 0
    zero = 0

    current = head

    while current is not None:

        if current.data > 0:
            positive += 1

        elif current.data < 0:
            negative += 1

        else:
            zero += 1

        current = current.next

    return positive, negative, zero


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

positive, negative, zero = count_values(head)

print("Positive values:", positive)
print("Negative values:", negative)
print("Zero values:", zero)