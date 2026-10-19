
def is_rotation(s, goal):
    if len(s) != len(goal):
        return False

    return goal in (s + s)


s = "abcde"
goal = "cdeab"

print("Original string:", s)
print("Target string:", goal)
print("Is rotation:", is_rotation(s, goal))
