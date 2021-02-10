from typing import List
from collections import deque

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        shapes = set()
        queue = []
        n = len(grid)
        m = len(grid[0])
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    shape = []
                    while queue:
                        row, col = queue.pop(0)
                        for nr, nc in (row + 1, col), (row - 1, col), (row, col +  1), (row, col - 1):
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                                queue.append((nr, nc))
                                shape.append((nr - r, nc - c))
                                grid[nr][nc] = 0
                    shapes.add(tuple(shape))
                    
        return len(shapes)


s = Solution()
ip = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
ans = s.numDistinctIslands(ip)
print(ans)