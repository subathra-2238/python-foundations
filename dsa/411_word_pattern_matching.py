
def word_pattern(pattern, sentence):
    words = sentence.split()

    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True


print(word_pattern("abba", "dog cat cat dog"))
print(word_pattern("abba", "dog cat cat fish"))
print(word_pattern("aaaa", "dog cat cat dog"))
