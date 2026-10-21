def hamming_distance(x, y):
    xor_result = x ^ y
    count = 0

    while xor_result > 0:
        count += xor_result & 1
        xor_result >>= 1

    return count


print("Distance:", hamming_distance(1, 4))
print("Distance:", hamming_distance(3, 1))
print("Distance:", hamming_distance(7, 7))
