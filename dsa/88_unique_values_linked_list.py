class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(40)
head.next.next.next.next.next = Node(30)
head.next.next.next.next.next.next = Node(50)


def find_unique_values(head):
    frequency = {}
    current = head

    # Count frequencies
    while current is not None:
        frequency[current.data] = frequency.get(current.data, 0) + 1
        current = current.next

    # Find values that occur once
    unique_values = []

    current = head

    while current is not None:
        if frequency[current.data] == 1:
            unique_values.append(current.data)

        current = current.next

    return unique_values


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

result = find_unique_values(head)

print("Values occurring only once:", result)