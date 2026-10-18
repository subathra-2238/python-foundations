
def longest_unique_substring(s):
    last_seen = {}
    left = 0
    max_length = 0
    best_substring = ""

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right

        if right - left + 1 > max_length:
            max_length = right - left + 1
            best_substring = s[left:right + 1]

    return best_substring


text = "abcabcbb"
result = longest_unique_substring(text)

print("String:", text)
print("Longest substring:", result)
print("Length:", len(result))
