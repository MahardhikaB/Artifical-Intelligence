graph = {
    'A': ['B', 'E', 'F'],
    'B': ['A', 'F', 'G'],
    'C': ['D', 'G'],
    'D': ['C', 'H'],
    'E': ['A', 'F'],
    'F': ['A', 'B', 'E'],
    'G': ['C', 'H'],
    'H': ['D', 'G']
}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Hasil penelusuran graf menggunakan BFS: ")
bfs(visited, graph, 'A')
