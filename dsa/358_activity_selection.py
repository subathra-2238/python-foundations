
def activity_selection(activities):
    activities.sort(key=lambda activity: activity[1])

    selected = []
    last_end = float("-inf")

    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


activities = [
    (1, 3),
    (2, 5),
    (4, 6),
    (6, 7),
    (5, 8),
    (8, 9)
]

result = activity_selection(activities)

print("Selected activities:", result)
print("Maximum activities:", len(result))
