
def simplify_path(path):
    stack = []

    for part in path.split("/"):
        if part == "" or part == ".":
            continue

        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return "/" + "/".join(stack)


print(simplify_path("/home//user/../documents/"))
print(simplify_path("/../"))
print(simplify_path("/a/./b/../../c/"))
print(simplify_path("/home/user"))
