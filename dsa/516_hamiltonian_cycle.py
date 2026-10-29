
def hamiltonian_cycle(graph):
    n = len(graph)
    path = [0]  # Start at vertex 0

    def is_safe(vertex):
        # Must connect to the previous vertex
        if graph[path[-1]][vertex] == 0:
            return False

        # Cannot visit a vertex twice
        if vertex in path:
            return False

        return True

    def backtrack():
        if len(path) == n:
            # The last vertex must connect back to 0
            return graph[path[-1]][path[0]] == 1

        for vertex in range(1, n):
            if is_safe(vertex):
                path.append(vertex)

                if backtrack():
                    return True

                # Undo the choice
                path.pop()

        return False

    if backtrack():
        return path + [path[0]]

    return None


graph1 = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

graph2 = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

print(hamiltonian_cycle(graph1))
print(hamiltonian_cycle(graph2))
