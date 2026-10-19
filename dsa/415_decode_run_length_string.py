
def decode_string(encoded):
    result = []
    i = 0

    while i < len(encoded):
        char = encoded[i]
        i += 1
        digits = ""

        while i < len(encoded) and encoded[i].isdigit():
            digits += encoded[i]
            i += 1

        if not digits:
            raise ValueError("Missing character count")

        result.append(char * int(digits))

    return "".join(result)


encoded = "a3b2c1"

print("Encoded string:", encoded)
print("Decoded string:", decode_string(encoded))
