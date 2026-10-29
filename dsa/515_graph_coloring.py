
def graph_coloring(graph, m):
    n = len(graph)
    colors = [0] * n  # 0 means uncolored

    def is_safe(vertex, color):
        for neighbor in range(n):
            if graph[vertex][neighbor] == 1:
                if colors[neighbor] == color:
                    return False
        return True

    def backtrack(vertex):
        if vertex == n:
            return True

        for color in range(1, m + 1):
            if is_safe(vertex, color):
                colors[vertex] = color

                if backtrack(vertex + 1):
                    return True

                # Undo the color choice
                colors[vertex] = 0

        return False

    if backtrack(0):
        return colors

    return None


graph1 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

graph2 = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

print(graph_coloring(graph1, 3))
print(graph_coloring(graph1, 2))
print(graph_coloring(graph2, 3))
