def count_jewels(jewels, stones):
    jewel_set = set(jewels)
    count = 0

    for stone in stones:
        if stone in jewel_set:
            count += 1

    return count


print(count_jewels("aA", "aAAbbbb"))
print(count_jewels("z", "ZZ"))
print(count_jewels("abc", "aabbcc"))
