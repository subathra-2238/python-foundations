
def restore_ip_addresses(s):
    result = []

    def backtrack(index, parts):
        if len(parts) == 4:
            if index == len(s):
                result.append(".".join(parts))
            return

        remaining_digits = len(s) - index
        remaining_parts = 4 - len(parts)

        # Each remaining part needs at least one digit
        if remaining_digits < remaining_parts:
            return

        # Each remaining part can contain at most three digits
        if remaining_digits > remaining_parts * 3:
            return

        for length in range(1, 4):
            segment = s[index:index + length]

            if len(segment) != length:
                break

            if length > 1 and segment[0] == "0":
                break

            if int(segment) > 255:
                break

            parts.append(segment)
            backtrack(index + length, parts)
            parts.pop()

    if 4 <= len(s) <= 12:
        backtrack(0, [])

    return result


print(restore_ip_addresses("25525511135"))
print(restore_ip_addresses("0000"))
print(restore_ip_addresses("101023"))
