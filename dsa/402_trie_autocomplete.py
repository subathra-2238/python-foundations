
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def autocomplete(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        results = []

        def collect(current, word):
            if current.is_end:
                results.append(word)

            for char, child in current.children.items():
                collect(child, word + char)

        collect(node, prefix)
        return sorted(results)


trie = Trie()

words = ["apple", "application", "apply", "apt", "banana"]

for word in words:
    trie.insert(word)

print("Suggestions:", trie.autocomplete("app"))
print("Suggestions:", trie.autocomplete("ba"))
print("Suggestions:", trie.autocomplete("cat"))
