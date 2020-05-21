from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix : return 0
        N , M , cnt , prev = len(matrix) , len(matrix[0]) , 0 , 0
        dp = [0] * (M + 1)
        # print(N,M)
        for i in range(1,N+1):
            for j in range(1,M+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == 1:
                    dp[j] = min(min(dp[j - 1], prev), dp[j]) + 1
                    cnt += dp[j]
                else:
                    dp[j] = 0
                prev = tmp
        return cnt

s = Solution()
# ip = [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
ip = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
ans = s.countSquares(ip)
print(ans)