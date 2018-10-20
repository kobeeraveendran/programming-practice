from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, parent, child):

        self.graph[parent].append(child)

    def bfs(self, start):
        queue = []

        visited = [False for x in range(len(self.graph))]

        queue.append(start)

        visited[start] = True

        while queue:
            curr = queue.pop(0)

            print(curr)

            for child in self.graph[curr]:
                if not visited[child]:
                    queue.append(child)
                    visited[child] = True

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)

print('BFS traversal of graph:')
graph.bfs(2)

print('BFS traversal of graph:')
graph.bfs(0)

print('BFS traversal of graph:')
graph.bfs(1)

print('BFS traversal of graph:')
graph.bfs(3)