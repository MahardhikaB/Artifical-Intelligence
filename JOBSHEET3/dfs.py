graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'C'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'H'],
    'G': ['H'],
    'H': ['F', 'G']
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Hasil penulusuran graf menggunakan DFS:")
dfs(visited, graph, 'A')