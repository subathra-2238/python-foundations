def number_to_words(num):
    if num == 0:
        return "Zero"

    ones = [
        "", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen",
        "Fifteen", "Sixteen", "Seventeen", "Eighteen",
        "Nineteen"
    ]

    tens = [
        "", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]

    def under_thousand(n):
        words = []

        if n >= 100:
            words.append(ones[n // 100])
            words.append("Hundred")
            n %= 100

        if n >= 20:
            words.append(tens[n // 10])
            n %= 10

        if n > 0:
            words.append(ones[n])

        return " ".join(words)

    parts = []

    for value, name in [
        (1_000_000_000, "Billion"),
        (1_000_000, "Million"),
        (1_000, "Thousand"),
        (1, "")
    ]:
        if num >= value:
            group = num // value
            num %= value

            if value == 1:
                parts.append(under_thousand(group))
            else:
                parts.append(under_thousand(group) + " " + name)

    return " ".join(parts)


print(number_to_words(12345))
print(number_to_words(100))
print(number_to_words(0))
