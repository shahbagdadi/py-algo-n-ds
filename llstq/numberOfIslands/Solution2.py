from typing import List
from collections import deque

class Solution:
    
    def isValid(self,r,c):
        return False if r < 0 or r >= self.rows or c < 0 or c >= self.cols or self.grid[r][c] != "1" else True 

    def dfs(self,r , c):
        if self.isValid(r,c):
            self.grid[r][c] = '#'
            self.dfs(r,c+1)
            self.dfs(r+1,c)
            self.dfs(r,c-1)
            self.dfs(r-1,c)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0 
        self.grid,self.rows,self.cols,cnt = grid,len(grid), len(grid[0]) ,0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "1":
                    cnt += 1
                    self.dfs(r,c)
        return cnt

ip1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
ip2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
a = s.numIslands(ip2)
print(a)