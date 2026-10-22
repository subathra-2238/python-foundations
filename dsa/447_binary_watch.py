def read_binary_watch(turned_on):
    times = []

    for hour in range(12):
        for minute in range(60):
            hour_bits = bin(hour).count("1")
            minute_bits = bin(minute).count("1")

            if hour_bits + minute_bits == turned_on:
                times.append(
                    f"{hour}:{minute:02d}"
                )

    return times


result = read_binary_watch(1)

print("Possible times:")
print(result)
print("Total:", len(result))
