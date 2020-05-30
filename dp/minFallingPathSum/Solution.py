from typing import List

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N , M = len(A) , len(A[0])
        dp = [0]*(M+2)
        for i in range(1,N+1):
            dp[0] , dp[M+1]= dp[1], dp[M]
            row = dp.copy()
            for j in range(1,M+1):
                row[j] = A[i-1][j-1] + min(dp[j-1], dp[j], dp[j+1])
            dp = row           
        return min(dp[1:M+1])

s = Solution()
ip = [[1,2,3],[4,5,6],[7,8,9]]
ans = s.minFallingPathSum(ip)
print(ans)