
from collections import Counter


def minimum_window(text, target):
    if not text or not target:
        return ""

    required = Counter(target)
    window = {}
    left = 0
    formed = 0
    needed = len(required)

    best_length = float("inf")
    best_start = 0

    for right, char in enumerate(text):
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        while formed == needed:
            length = right - left + 1

            if length < best_length:
                best_length = length
                best_start = left

            left_char = text[left]
            window[left_char] -= 1

            if (
                left_char in required
                and window[left_char] < required[left_char]
            ):
                formed -= 1

            left += 1

    if best_length == float("inf"):
        return ""

    return text[best_start:best_start + best_length]


text = "ADOBECODEBANC"
target = "ABC"

print("Minimum window:", minimum_window(text, target))
