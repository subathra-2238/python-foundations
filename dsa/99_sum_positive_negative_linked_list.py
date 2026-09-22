class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(-5)
head.next.next = Node(20)
head.next.next.next = Node(-15)
head.next.next.next.next = Node(0)


def sum_positive_negative(head):
    positive_sum = 0
    negative_sum = 0

    current = head

    while current is not None:

        if current.data > 0:
            positive_sum += current.data

        elif current.data < 0:
            negative_sum += current.data

        current = current.next

    return positive_sum, negative_sum


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

positive_sum, negative_sum = sum_positive_negative(head)

print("Sum of positive values:", positive_sum)
print("Sum of negative values:", negative_sum)