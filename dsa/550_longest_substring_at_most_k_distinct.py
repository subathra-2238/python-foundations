
def longest_substring_k_distinct(s, k):
    if not s or k <= 0:
        return 0

    left = 0
    max_length = 0
    frequency = {}

    for right in range(len(s)):
        char = s[right]

        frequency[char] = frequency.get(char, 0) + 1

        while len(frequency) > k:
            left_char = s[left]
            frequency[left_char] -= 1

            if frequency[left_char] == 0:
                del frequency[left_char]

            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_substring_k_distinct("eceba", 2))
print(longest_substring_k_distinct("aa", 1))
print(longest_substring_k_distinct("aabbcc", 2))
print(longest_substring_k_distinct("abc", 0))
