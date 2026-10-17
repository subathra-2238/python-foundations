
def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0

    if m > n:
        return -1

    base = 256
    prime = 101

    pattern_hash = 0
    window_hash = 0
    highest_power = pow(base, m - 1, prime)

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            window_hash = (
                base * (window_hash - ord(text[i]) * highest_power)
                + ord(text[i + m])
            ) % prime

    return -1


text = "ABCCDDAEFG"
pattern = "DAE"

position = rabin_karp(text, pattern)

if position != -1:
    print("Pattern found at index:", position)
else:
    print("Pattern not found")
