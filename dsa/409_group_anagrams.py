
from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = group_anagrams(words)

print("Grouped anagrams:")
for group in result:
    print(group)
