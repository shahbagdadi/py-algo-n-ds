from typing import List
import sys

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid) , len(grid[0])
        dp = [0] * N
        dp[0] = grid[0][0]
        for i in range(1, N):
            dp[i] = dp[i-1] + grid[0][i]
        print(dp)
        for i in range(1,M):
            dp[0] += grid[i][0]
            for j in range(1,N): 
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
            print(dp)
        return dp[N-1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        N, M = len(grid) , len(grid[0])
        for i in range(1, M):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for i in range(1,N):
            grid[i][0] += grid[i-1][0]
            for j in range(1,M):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[N-1][M-1]



ip = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

s = Solution()
ans = s.minPathSum2(ip)
print(ans)