#from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = {}

    def addEdge(parent, child):
        if graph[parent]:
            graph[parent].append(child)
        
        else:
            graph[parent] = [child]

    def bfs(start):
        queue = []

        queue.append(start)

        while queue:
            curr = queue.pop()

            print(curr + ' ')

            queue.append(self.graph[curr])

graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(2, 3)
graph.addEdge(3, 3)

print('BFS traversal of graph:')
graph.bfs(2)