
def largest_rectangle_area(heights):
    stack = []
    max_area = 0

    # Add a zero-height bar to process remaining bars
    for i in range(len(heights) + 1):
        current_height = heights[i] if i < len(heights) else 0

        while stack and heights[stack[-1]] > current_height:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area


print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))
print(largest_rectangle_area([2, 4]))
print(largest_rectangle_area([2, 2, 2, 2]))
