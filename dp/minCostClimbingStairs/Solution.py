from functools import lru_cache
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        
        @lru_cache(None)
        def climb(i):
            if i == N-1 or i == N-2:
                return cost[i]
            return min(climb(i+1) , climb(i+2))+ cost[i]
        return min(climb(0),climb(1))


    def DPminCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * N
        dp[0],dp[1] = cost[0], cost[1]
        for i in range(2,N):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # print(dp)
        return min(dp[N-1],dp[N-2])

s = Solution()
ip = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
ans = s.minCostClimbingStairs(ip)
print(ans)

ans = s.DPminCostClimbingStairs(ip)
print(ans)