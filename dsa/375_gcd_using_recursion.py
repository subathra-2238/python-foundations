
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


a = 48
b = 18

print("First number:", a)
print("Second number:", b)
print("GCD:", gcd(a, b))
