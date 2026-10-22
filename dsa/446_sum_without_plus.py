def get_sum(a, b):
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    return a


print("Sum of 5 and 7:", get_sum(5, 7))
print("Sum of 12 and 8:", get_sum(12, 8))
print("Sum of 10 and 15:", get_sum(10, 15))
