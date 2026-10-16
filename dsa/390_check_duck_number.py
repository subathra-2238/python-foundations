
def is_duck_number(number):
    text = str(number)

    if number <= 0 or text[0] == "0":
        return False

    return "0" in text


number = 1023

print("Number:", number)

if is_duck_number(number):
    print("It is a Duck number.")
else:
    print("It is not a Duck number.")
