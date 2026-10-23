from collections import Counter


def common_characters(words):
    common = Counter(words[0])

    for word in words[1:]:
        common &= Counter(word)

    result = []

    for char, count in sorted(common.items()):
        result.extend([char] * count)

    return result


print(common_characters(["bella", "label", "roller"]))
print(common_characters(["cool", "lock", "cook"]))
