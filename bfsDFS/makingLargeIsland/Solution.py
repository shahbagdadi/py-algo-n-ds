from typing import List
from collections import deque


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def neighbor(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in neighbor(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        # DFS every island and give it an index of island. The index is set in the grid
        index = 2 # since grid has 0,1 start the island index from 2
        areas = {0: 0} # island with index 0 has an area of 0
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in neighbor(x, y)) # set removes duplicate island index
                    res = max(res, sum(areas[index] for index in possible) + 1) # get sum of all the possible connected island index
        return res





s = Solution()
ip = [[0,0],[0,1]]
ans = s.largestIsland(ip)
print(ans)