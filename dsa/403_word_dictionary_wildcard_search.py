
class WordDictionary:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def search(self, pattern):
        for word in self.words:
            if len(word) != len(pattern):
                continue

            match = True

            for i in range(len(pattern)):
                if pattern[i] != "." and pattern[i] != word[i]:
                    match = False
                    break

            if match:
                return True

        return False


dictionary = WordDictionary()

dictionary.add_word("bad")
dictionary.add_word("dad")
dictionary.add_word("mad")

print("Search bad:", dictionary.search("bad"))
print("Search .ad:", dictionary.search(".ad"))
print("Search b..:", dictionary.search("b.."))
print("Search b.dly:", dictionary.search("b.dly"))
