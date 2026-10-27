
def asteroid_collision(asteroids):
    stack = []

    for asteroid in asteroids:
        alive = True

        while (
            alive
            and asteroid < 0
            and stack
            and stack[-1] > 0
        ):
            if stack[-1] < -asteroid:
                stack.pop()
            elif stack[-1] == -asteroid:
                stack.pop()
                alive = False
            else:
                alive = False

        if alive:
            stack.append(asteroid)

    return stack


print(asteroid_collision([5, 10, -5]))
print(asteroid_collision([8, -8]))
print(asteroid_collision([10, 2, -5]))
print(asteroid_collision([-2, -1, 1, 2]))
