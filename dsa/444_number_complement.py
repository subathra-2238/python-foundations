def find_complement(n):
    if n == 0:
        return 1

    mask = 0
    temp = n

    while temp > 0:
        mask = (mask << 1) | 1
        temp >>= 1

    return n ^ mask


print("Complement of 5:", find_complement(5))
print("Complement of 10:", find_complement(10))
print("Complement of 7:", find_complement(7))
