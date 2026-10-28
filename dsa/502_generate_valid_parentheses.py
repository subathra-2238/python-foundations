
def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add an opening parenthesis if available
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        # Add a closing parenthesis only when it stays valid
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


print(generate_parentheses(1))
print(generate_parentheses(2))
print(generate_parentheses(3))
