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


def find_least_frequent(head):
    frequency = {}
    current = head

    # Count frequencies
    while current is not None:
        frequency[current.data] = frequency.get(current.data, 0) + 1
        current = current.next

    # Find minimum frequency
    least_frequent = None
    min_count = float("inf")

    for value, count in frequency.items():
        if count < min_count:
            min_count = count
            least_frequent = value

    return least_frequent, min_count


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

value, count = find_least_frequent(head)

print("Least frequent value:", value)
print("Frequency:", count)