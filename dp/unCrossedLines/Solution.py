from typing import List
from collections import defaultdict

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M,N=len(A),len(B)
        dp=[[0]*(N+1) for _ in range(M+1)]
        for m in range(M):
            for n  in range(N):
                if A[m] == B[n] :
                    dp[m+1][n+1] = dp[m][n] + 1
                else:
                    dp[m+1][n+1] = max(dp[m][n+1], dp[m+1][n])
        # print (dp)
        return dp[-1][-1]

s = Solution()
ip1 = [3,3,1,3]
ip2 =  [1,3,2,3,3,1]
ans = s.maxUncrossedLines(ip1,ip2)
print(ans)