def find_lus_length(a, b):
    if a == b:
        return -1

    return max(len(a), len(b))


print(find_lus_length("aba", "cdc"))
print(find_lus_length("aaa", "aaa"))
print(find_lus_length("abcd", "abc"))
