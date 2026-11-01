
# DSA 549: Minimum Window Substring
# Sliding Window + Hash Map

from collections import Counter

def min_window(s, t):
    if not s or not t or len(t) > len(s):
        return ""

    required = Counter(t)
    window = {}

    left = 0
    formed = 0
    required_count = len(required)

    minimum_length = float("inf")
    result = ""

    for right in range(len(s)):
        char = s[right]

        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        # Shrink the window when all requirements are met
        while formed == required_count:
            current_length = right - left + 1

            if current_length < minimum_length:
                minimum_length = current_length
                result = s[left:right + 1]

            left_char = s[left]
            window[left_char] -= 1

            if (left_char in required and
                    window[left_char] < required[left_char]):
                formed -= 1

            left += 1

    return result


print(min_window("ADOBECODEBANC", "ABC"))
print(min_window("a", "a"))
print(min_window("a", "aa"))
