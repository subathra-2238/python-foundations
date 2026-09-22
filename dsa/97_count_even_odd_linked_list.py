class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(25)
head.next.next = Node(30)
head.next.next.next = Node(41)
head.next.next.next.next = Node(50)


def count_even_odd(head):
    even_count = 0
    odd_count = 0

    current = head

    while current is not None:

        if current.data % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        current = current.next

    return even_count, odd_count


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