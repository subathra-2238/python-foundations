
def reverse_number(n, reversed_num=0):
    if n == 0:
        return reversed_num

    reversed_num = reversed_num * 10 + n % 10
    return reverse_number(n // 10, reversed_num)


number = 1234

print("Original number:", number)
print("Reversed number:", reverse_number(abs(number)))
