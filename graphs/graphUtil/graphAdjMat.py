from typing import List
from collections import deque
from collections import defaultdict

# A class to represent a graph. A graph
# is the list of the adjacency Matrix.
# Size of the array will be the no. of the
# vertices "V"


class Graph:
    def __init__(self, vertices, directed=True):
        self.V = vertices
        self.adjMatrix = []
        self.directed = directed
        for i in range(self.V):
            self.adjMatrix.append([0 for i in range(self.V)])

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        if src == dest:
            print(f"Same vertex {src} and {dest}")
        self.adjMatrix[src][dest] = 1
        if not self.directed:
            self.adjMatrix[dest][src] = 1

    # Function to print the graph adj list
    def print_adj_list(self):
        for k in self.graph.keys():
            print(f"Adjacency list of vertex {k}\n {k}", end="")
            for n in self.graph[k]:
                print(f" -> {n}", end="")
            print(" \n")

    def print_adj_mat(self):
        print(self.adjMatrix)

    # Breadth First Traversal of graph
    def BFS(self, root):
        q = deque([root])
        visited = set([root])
        while q:
            node = q.pop()
            print(f'{node} => ', end="")
            for i, child in enumerate(self.adjMatrix[node]):
                if child == 1 and i not in visited:
                    visited.add(i)
                    q.appendleft(i)


g = Graph(5, True)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 4)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_adj_mat()
print('====== BFS  =====')
g.BFS(0)
print('\n')
