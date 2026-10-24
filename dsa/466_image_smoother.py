def image_smoother(img):
    rows = len(img)
    cols = len(img[0])
    result = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            total = 0
            count = 0

            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        total += img[nr][nc]
                        count += 1

            result[r][c] = total // count

    return result


image = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

for row in image_smoother(image):
    print(row)
