from typing import List
import sys
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def neighbors(node):
            r , c = node
            steps = ((r-1,c) , (r,c+1) , (r+1, c), (r, c-1))
            for nr,nc in steps:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1: 
                    yield (nr , nc)
                
        def bfs(root) :
            q.appendleft(root)
            v.add(root)
            area = 0
            while q :
                node = q.pop()
                area += 1
                for neighbor in neighbors(node):
                    if neighbor not in v:
                        q.appendleft(neighbor)
                        v.add(neighbor)             
            return area

        max_area , R , C = 0 , len(grid) , len(grid[0])
        q , v = deque(), set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in v:
                    max_area = max(max_area, bfs((r,c)))
        return max_area


ip = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

s = Solution()
ans = s.maxAreaOfIsland(ip)
print(ans)