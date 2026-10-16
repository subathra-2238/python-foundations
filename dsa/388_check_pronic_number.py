
def is_pronic(n, i=0):
    if i * (i + 1) == n:
        return True

    if i * (i + 1) > n:
        return False

    return is_pronic(n, i + 1)


number = 12

print("Number:", number)

if is_pronic(number):
    print("It is a Pronic number.")
else:
    print("It is not a Pronic number.")
