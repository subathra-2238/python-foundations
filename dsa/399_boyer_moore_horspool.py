
def boyer_moore_horspool(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    if m > n:
        return -1

    shift = {}

    for i in range(m - 1):
        shift[pattern[i]] = m - 1 - i

    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift.get(text[i + m - 1], m)

    return -1


text = "HERE IS A SIMPLE EXAMPLE"
pattern = "EXAMPLE"

position = boyer_moore_horspool(text, pattern)

if position != -1:
    print("Pattern found at index:", position)
else:
    print("Pattern not found")
