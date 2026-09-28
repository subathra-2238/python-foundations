class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(40)
head.next.next.next.next.next = Node(20)
head.next.next.next.next.next.next = Node(30)


def find_most_frequent(head):
    frequency = {}
    current = head

    # Count frequencies
    while current is not None:
        frequency[current.data] = frequency.get(current.data, 0) + 1
        current = current.next

    # Find maximum frequency
    most_frequent = None
    max_count = 0

    for value, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = value

    return most_frequent, max_count


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

value, count = find_most_frequent(head)

print("Most frequent value:", value)
print("Frequency:", count)