# Break and Continue

print("Break Example")

for number in range(1, 11):
    if number == 6:
        break
    print(number)


print("\nContinue Example")

for number in range(1, 11):
    if number == 5:
        continue
    print(number)