
def count_and_say(n):
    if n <= 0:
        return ""

    result = "1"

    for _ in range(n - 1):
        next_result = []
        count = 1

        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                count += 1
            else:
                next_result.append(str(count))
                next_result.append(result[i - 1])
                count = 1

        next_result.append(str(count))
        next_result.append(result[-1])

        result = "".join(next_result)

    return result


for i in range(1, 6):
    print(f"Term {i}: {count_and_say(i)}")
