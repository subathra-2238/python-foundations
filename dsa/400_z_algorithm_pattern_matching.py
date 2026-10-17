
def z_algorithm(s):
    n = len(s)
    z = [0] * n
    left = right = 0

    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])

        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1

    return z


def find_pattern(text, pattern):
    if not pattern:
        return 0

    combined = pattern + "$" + text
    z = z_algorithm(combined)

    for i in range(len(pattern) + 1, len(combined)):
        if z[i] >= len(pattern):
            return i - len(pattern) - 1

    return -1


text = "ABABCABAB"
pattern = "CAB"

position = find_pattern(text, pattern)
print("Pattern found at index:", position)
