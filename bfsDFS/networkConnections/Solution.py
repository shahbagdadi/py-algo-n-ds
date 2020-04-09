from typing import List
from collections import defaultdict
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/No-TarjanDFS-detailed-explanation-O(orEor)-solution-(I-like-this-question)


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        def buildGraph(connections):
            graph = defaultdict(list)
            for c in connections:  # build bi directional graph
                graph[c[0]].append(c[1])
                graph[c[1]].append(c[0])
            return graph

        graph = buildGraph(connections)
        # print(graph)
        # sort all connections in tuple 0->1 == 1->0
        uniq_conns = set(map(tuple, (map(sorted, connections))))
        # print(uniq_conns)
        rank = [-2] * n  # mark all connections as unvisited

        def dfs(node, depth):
            if rank[node] >= 0:     # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue                            # visiting from parent connection so continue
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:                 # this indicates there is a cycle
                    uniq_conns.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            return min_back_depth

        # since this is a connected graph, we don't have to loop over all nodes.
        dfs(0, 0)
        return list(uniq_conns)


s = Solution()
conns = s.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
print(conns)
