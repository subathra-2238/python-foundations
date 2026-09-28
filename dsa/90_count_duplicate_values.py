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


def count_duplicate_values(head):
    frequency = {}
    current = head

    # Count frequencies
    while current is not None:
        frequency[current.data] = frequency.get(current.data, 0) + 1
        current = current.next

    # Count values appearing more than once
    duplicate_count = 0

    for count in frequency.values():
        if count > 1:
            duplicate_count += 1

    return duplicate_count


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

result = count_duplicate_values(head)

print("Number of duplicate values:", result)