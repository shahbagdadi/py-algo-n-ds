from typing import List
from collections import deque
from collections import defaultdict

# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"


class Graph:
    def __init__(self, vertices, directed=True):
        self.V = vertices
        self.graph = defaultdict(list)
        self.directed = directed

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)

    # Function to print the graph adj list
    def print_adj_list(self):
        for k in self.graph.keys():
            print(f"Adjacency list of vertex {k}\n {k}", end="")
            for n in self.graph[k]:
                print(f" -> {n}", end="")
            print(" \n")

    # Breadth First Traversal of graph
    def BFS(self, root):
        q = deque([root])
        visited = set([root])
        while q:
            node = q.pop()
            print(f'{node} => ', end="")
            for child in self.graph[node]:
                if child not in visited:
                    visited.add(child)
                    q.appendleft(child)

    # Iterative Depth First Traversal of graph
    def DFS(self, root):
        stack = [root]
        visited = set([root])
        while stack:
            node = stack.pop()
            print(f'{node} => ', end="")
            for child in self.graph[node]:
                if child not in visited:
                    visited.add(child)
                    stack.append(child)

    # Recursive Depth First Traversal of graph
    def DFS_recursive(self, root, visited=set()):
        visited.add(root)
        print(f'{root} => ', end="")
        for child in self.graph[root]:
            if child not in visited:
                visited.add(child)
                self.DFS_recursive(child, visited)


g = Graph(5, True)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 4)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_adj_list()
print('====== BFS  =====')
g.BFS(0)
print('\n')
print('====== DFS  Iterative =====')
g.DFS(0)
print('\n')
print('====== DFS  Recursive =====')
g.DFS_recursive(0)
