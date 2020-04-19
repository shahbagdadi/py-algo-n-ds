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



ip = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

s = Solution()
ans = s.minPathSum(ip)
print(ans)