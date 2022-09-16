graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'H'],
    'G': ['H'],
    'H': ['F', 'G']
}

visited = [] #List to keep track of visited nodes.
queue = []    #Initialize a queue

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