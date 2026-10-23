from collections import Counter


def frequency_sort(s):
    frequency = Counter(s)

    sorted_chars = sorted(
        s,
        key=lambda char: (-frequency[char], char)
    )

    return "".join(sorted_chars)


print(frequency_sort("tree"))
print(frequency_sort("cccaaa"))
print(frequency_sort("banana"))
