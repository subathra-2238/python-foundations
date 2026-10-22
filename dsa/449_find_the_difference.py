def find_difference(s, t):
    result = 0

    for char in s:
        result ^= ord(char)

    for char in t:
        result ^= ord(char)

    return chr(result)


print("Extra character:", find_difference("abcd", "abcde"))
print("Extra character:", find_difference("aabb", "ababa"))
