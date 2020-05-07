
from typing import List
from collections import Counter
from typing import List

class Solution:
    # Explanation - https://leetcode.com/problems/trapping-rain-water-ii/discuss/89472/Visualization-No-Code
    def trap(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        import heapq    
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        result = 0
        while heap:
            height, i, j = heapq.heappop(heap)    
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height-heightMap[x][y])
                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))
                    visited[x][y] = 1
        return result

s = Solution()
ip = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
ans = s.trap(ip)
print(ans)
                
