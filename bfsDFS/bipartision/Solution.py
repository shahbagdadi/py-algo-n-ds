from typing import List
from collections import defaultdict

class Solution:
    # T - O(N + E)   S - O(N + E)
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for hate in dislikes:
            graph[hate[0]].append(hate[1])
            graph[hate[1]].append(hate[0])
        color = {}

        def dfs(node , c = 0) :
            if node in color:
                return color[node] == c
            color[node] = c
            return all( dfs(node, c ^ 1) for node in graph[node])
        
        return all(dfs(node) for node in range(1,N+1) if node not in color)
        

s = Solution()
ip = [[1,2],[1,3],[2,4]]
ans = s.possibleBipartition(4,ip)
print(ans)