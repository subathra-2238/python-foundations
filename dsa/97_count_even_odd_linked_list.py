class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(25)
head.next.next = Node(8)
head.next.next.next = Node(13)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(7)


def count_even_odd(head):
    even = 0
    odd = 0

    current = head

    while current is not None:

        if current.data % 2 == 0:
            even += 1
        else:
            odd += 1

        current = current.next

    return even, odd


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

even, odd = count_even_odd(head)

print("Even values:", even)
print("Odd values:", odd)