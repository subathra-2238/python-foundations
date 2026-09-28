class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def start_of_longest_decreasing_run(head):
    if head is None:
        return None

    current = head
    current_length = 1

    longest = 1
    longest_start = head.data

    current_start = head.data

    while current.next is not None:
        if current.next.data < current.data:
            current_length += 1
        else:
            current_length = 1
            current_start = current.next.data

        if current_length > longest:
            longest = current_length
            longest_start = current_start

        current = current.next

    return longest_start


# Create linked list
head = Node(30)
head.next = Node(25)
head.next.next = Node(20)
head.next.next.next = Node(28)
head.next.next.next.next = Node(15)
head.next.next.next.next.next = Node(10)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(12)

result = start_of_longest_decreasing_run(head)

print("Starting value:", result)