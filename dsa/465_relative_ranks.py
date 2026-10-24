def find_relative_ranks(scores):
    sorted_scores = sorted(scores, reverse=True)
    rank_map = {}

    for index, score in enumerate(sorted_scores):
        if index == 0:
            rank_map[score] = "Gold Medal"
        elif index == 1:
            rank_map[score] = "Silver Medal"
        elif index == 2:
            rank_map[score] = "Bronze Medal"
        else:
            rank_map[score] = str(index + 1)

    return [rank_map[score] for score in scores]


scores = [5, 4, 3, 2, 1]
print(find_relative_ranks(scores))

scores = [10, 3, 8, 9, 4]
print(find_relative_ranks(scores))
