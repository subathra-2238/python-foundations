
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


a = 12
b = 18

print("First number:", a)
print("Second number:", b)
print("LCM:", lcm(a, b))
