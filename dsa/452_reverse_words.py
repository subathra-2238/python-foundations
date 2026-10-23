def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)


print(reverse_words("Python is fun"))
print(reverse_words("I love learning DSA"))
print(reverse_words("  hello   world  "))
