from collections import Counter


def can_construct(note, magazine):
    note_count = Counter(note)
    magazine_count = Counter(magazine)

    for char, count in note_count.items():
        if magazine_count[char] < count:
            return False

    return True


print(can_construct("a", "b"))
print(can_construct("aa", "ab"))
print(can_construct("aa", "aab"))
