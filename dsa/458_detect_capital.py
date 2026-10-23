def detect_capital_use(word):
    return (
        word.isupper()
        or word.islower()
        or word.istitle()
    )


print(detect_capital_use("USA"))
print(detect_capital_use("leetcode"))
print(detect_capital_use("Google"))
print(detect_capital_use("FlaG"))
