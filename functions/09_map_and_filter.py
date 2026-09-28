# map() and filter()

numbers = [1, 2, 3, 4, 5]

# map() - apply a function to every item
squares = list(map(lambda number: number * number, numbers))

print("Numbers:", numbers)
print("Squares:", squares)


# filter() - keep items that satisfy a condition
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print("Even numbers:", even_numbers)