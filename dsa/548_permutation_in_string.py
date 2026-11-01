
# DSA 548: Permutation in String
# Fixed-Size Sliding Window

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    required = [0] * 26
    window = [0] * 26

    # Count characters in s1
    for char in s1:
        required[ord(char) - ord('a')] += 1

    # Create the first window
    for char in s2[:len(s1)]:
        window[ord(char) - ord('a')] += 1

    if required == window:
        return True

    # Slide the window
    for right in range(len(s1), len(s2)):

        # Add incoming character
        window[ord(s2[right]) - ord('a')] += 1

        # Remove outgoing character
        left = right - len(s1)
        window[ord(s2[left]) - ord('a')] -= 1

        if required == window:
            return True

    return False


print(check_inclusion("ab", "eidbaooo"))
print(check_inclusion("ab", "eidboaoo"))
print(check_inclusion("adc", "dcda"))
