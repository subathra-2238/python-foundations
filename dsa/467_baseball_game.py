def cal_points(operations):
    scores = []

    for operation in operations:
        if operation == "C":
            scores.pop()

        elif operation == "D":
            scores.append(2 * scores[-1])

        elif operation == "+":
            scores.append(scores[-1] + scores[-2])

        else:
            scores.append(int(operation))

    return sum(scores)


operations = ["5", "2", "C", "D", "+"]
print("Final score:", cal_points(operations))

operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
print("Final score:", cal_points(operations))
