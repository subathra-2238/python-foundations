
# DSA 547: Longest Repeating Character Replacement
# Sliding Window Algorithm

def character_replacement(s, k):
    left = 0
    max_frequency = 0
    max_length = 0

    frequency = {}

    for right in range(len(s)):

        char = s[right]

        frequency[char] = frequency.get(char, 0) + 1

        max_frequency = max(
            max_frequency,
            frequency[char]
        )

        # Calculate characters that need replacement
        window_length = right - left + 1

        if window_length - max_frequency > k:
            frequency[s[left]] -= 1
            left += 1

        max_length = max(
            max_length,
            right - left + 1
        )

    return max_length


print(character_replacement("AABABBA", 1))
print(character_replacement("ABAB", 2))
print(character_replacement("AAAA", 0))
