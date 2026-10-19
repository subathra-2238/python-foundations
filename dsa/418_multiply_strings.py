def multiply_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    m = len(num1)
    n = len(num2)
    result = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            product = int(num1[i]) * int(num2[j])
            total = product + result[i + j + 1]

            result[i + j + 1] = total % 10
            result[i + j] += total // 10

    answer = "".join(map(str, result)).lstrip("0")
    return answer or "0"


print("Product:", multiply_strings("123", "456"))
