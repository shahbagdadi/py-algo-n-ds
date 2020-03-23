from typing import List
from collections import deque

class Solution:
    paths = [[0,1],[1,0],[0,-1],[-1,0]]
    def isValid(self,r,c):
        return False if r < 0 or r >= self.rows or c < 0 or c >= self.cols else True 
        
    def bfs(self,r,c):
        q = deque()
        q.append((r,c))
        self.visited[r][c] = True
        self.grid[r][c] = "0"
        while len(q) > 0:
            # print(q)
            cr,cc = q.pop()
            # print(f'{cr} , {cc}')
            for p in self.paths:
                nr , nc = cr + p[0] , cc + p[1]
                if self.isValid(nr,nc) and self.grid[nr][nc] == "1" and not self.visited[nr][nc]:
                    self.visited[nr][nc] = True
                    self.grid[nr][nc] = "0"
                    q.append((nr,nc))
                    # print(self.grid)
        return None

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0 
        self.grid,self.rows,self.cols,cnt = grid,len(grid), len(grid[0]) ,0
        self.visited = [[False for i in range(self.cols)] for j in range(self.rows)]
        # print(self.visited)
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "1":
                    cnt += 1
                    self.bfs(r,c)
                # print(self.grid)
        return cnt

ip1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
ip2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
a = s.numIslands(ip2)
print(a)