def count_set_bits(n):
    count = 0

    while n > 0:
        count += n & 1
        n >>= 1

    return count


print("13:", count_set_bits(13))
print("7:", count_set_bits(7))
print("8:", count_set_bits(8))
print("0:", count_set_bits(0))
