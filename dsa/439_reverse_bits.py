def reverse_bits(n):
    result = 0

    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1

    return result


number = 13
print("Original number:", number)
print("Reversed bits:", reverse_bits(number))
