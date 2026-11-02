
def can_allocate(pages, students, limit):
    allocated_students = 1
    current_pages = 0

    for page in pages:
        if page > limit:
            return False

        if current_pages + page > limit:
            allocated_students += 1
            current_pages = page
        else:
            current_pages += page

    return allocated_students <= students


def book_allocation(pages, students):
    n = len(pages)

    if students <= 0 or students > n:
        return -1

    left = max(pages)
    right = sum(pages)

    while left < right:
        mid = (left + right) // 2

        if can_allocate(pages, students, mid):
            right = mid
        else:
            left = mid + 1

    return left


print(book_allocation([12, 34, 67, 90], 2))
print(book_allocation([10, 20, 30, 40], 2))
print(book_allocation([5, 10, 15], 3))
print(book_allocation([10, 20], 3))
