
def is_palindrome(text, left, right):
    if left >= right:
        return True

    if text[left] != text[right]:
        return False

    return is_palindrome(text, left + 1, right - 1)


text = "madam"

result = is_palindrome(text, 0, len(text) - 1)

print("String:", text)

if result:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
