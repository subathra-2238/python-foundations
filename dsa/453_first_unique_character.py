from collections import Counter


def first_unique_character(s):
    frequency = Counter(s)

    for index, char in enumerate(s):
        if frequency[char] == 1:
            return index

    return -1


print(first_unique_character("leetcode"))
print(first_unique_character("loveleetcode"))
print(first_unique_character("aabb"))
