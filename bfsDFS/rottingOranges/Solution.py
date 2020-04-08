from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # generator for neighbors
        def neighbors(r,c):
            steps = ((r-1,c) , (r+1, c), (r , c-1), (r, c+1))
            for nr, nc in steps:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        R , C = len(grid) , len(grid[0])
        q = deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:                    # add all rotten oranges to queue with depth as 0
                    q.appendleft((r, c, 0)) 
        
        d = 0
        while q :
            r,c,d = q.pop()
            for nr, nc in neighbors(r,c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.appendleft((nr,nc,d+1))

        if any(1 in row for row in grid): return -1
        return d



s = Solution()
ans = s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(ans)