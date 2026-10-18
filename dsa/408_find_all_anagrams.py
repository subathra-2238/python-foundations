
from collections import Counter


def find_anagrams(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return []

    target = Counter(pattern)
    window = Counter(text[:m])
    result = []

    if window == target:
        result.append(0)

    for right in range(m, n):
        window[text[right]] += 1

        left_char = text[right - m]
        window[left_char] -= 1

        if window[left_char] == 0:
            del window[left_char]

        if window == target:
            result.append(right - m + 1)

    return result


text = "cbaebabacd"
pattern = "abc"

print("Anagram starting indices:", find_anagrams(text, pattern))
