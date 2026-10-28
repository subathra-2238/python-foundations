
def letter_combinations(digits):
    if not digits:
        return []

    keypad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append("".join(path))
            return

        letters = keypad[digits[index]]

        for letter in letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result


print(letter_combinations("23"))
print(letter_combinations("7"))
print(letter_combinations(""))
