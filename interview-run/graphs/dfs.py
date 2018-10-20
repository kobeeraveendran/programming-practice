from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = [False for x in range(len(self.graph))]

        stack = [start]

        while stack):
            curr = stack.pop()
            
            

