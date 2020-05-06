from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]: return -1
        M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1) # count num of building to prune quickly
        hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]     #dp list
        
        def neighbors(x,y,visited):
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                    yield i,j

        def BFS(start_x, start_y):
            visited = [[False] * N for k in range(M)]
            visited[start_x][start_y], count1, queue = True, 1, deque([(start_x, start_y, 0)]) # (x,y,distance_from_1)
            while queue:
                x, y, dist = queue.pop()
                for i, j in neighbors(x,y,visited):
                    visited[i][j] = True
                    if not grid[i][j]:              # if it is a '0'
                        queue.appendleft((i, j, dist + 1))
                        hit[i][j] += 1
                        distSum[i][j] += dist + 1
                    elif grid[i][j] == 1:
                        count1 += 1
            return count1 == buildings  
        
        # BFS for all '1' nodes
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x, y): return -1     # return -1 if all buildings cannot be reached
        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])

s = Solution()
ip = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
ans = s.shortestDistance(ip)
print(ans)