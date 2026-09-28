# Global Keyword

score = 10


def increase_score():
    global score
    score += 5


print("Before:", score)

increase_score()

print("After:", score)