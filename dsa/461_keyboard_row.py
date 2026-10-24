def find_words(words):
    rows = [
        set("qwertyuiop"),
        set("asdfghjkl"),
        set("zxcvbnm")
    ]

    result = []

    for word in words:
        letters = set(word.lower())

        for row in rows:
            if letters.issubset(row):
                result.append(word)
                break

    return result


words = ["Hello", "Alaska", "Dad", "Peace"]
print(find_words(words))
