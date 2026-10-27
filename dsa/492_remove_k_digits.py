
def remove_k_digits(num, k):
    stack = []

    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    # If removals remain, remove digits from the end
    while k > 0:
        stack.pop()
        k -= 1

    # Remove leading zeros
    result = "".join(stack).lstrip("0")

    return result if result else "0"


print(remove_k_digits("1432219", 3))
print(remove_k_digits("10200", 1))
print(remove_k_digits("10", 2))
print(remove_k_digits("12345", 2))
