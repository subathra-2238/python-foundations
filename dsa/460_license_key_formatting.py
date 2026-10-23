def license_key_formatting(s, k):
    cleaned = s.replace("-", "").upper()

    first_group_size = len(cleaned) % k
    groups = []

    if first_group_size:
        groups.append(cleaned[:first_group_size])

    for i in range(first_group_size, len(cleaned), k):
        groups.append(cleaned[i:i + k])

    return "-".join(groups)


print(license_key_formatting("5F3Z-2e-9-w", 4))
print(license_key_formatting("2-5g-3-J", 2))
print(license_key_formatting("---", 3))
