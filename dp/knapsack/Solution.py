from typing import List
from functools import lru_cache

class Solution:

    # T - O(n * w)    S - O(n * w)
    def knapSackDP(self, wt: List, val: List, W: int) -> int:
        dp = [[0 for x in range(W + 1)] for x in range(len(wt) + 1)]  # init DP
        # Table in bottom up manner
        for n in range(len(wt) + 1):                            # Loop 1
            for w in range(W + 1):                              # Loop 2
                if n == 0 or w == 0:                            # base cond
                    dp[n][w] = 0
                elif wt[n-1] <= w:
                    dp[n][w] = max(val[n-1] + dp[n-1][w-wt[n-1]], dp[n-1][w])
                else:
                    dp[n][w] = dp[n-1][w]
        return dp[n][W]

    #  T - O(2^n)    S - O(n)
    #  lru_cache T - O(n * w)    S - O(n * w)
    def knapSackR(self, wt: List, val: List, W: int) -> int:
        # @lru_cache(None)
        def helper( W, n):
            if n == 0 or W <= 0:  # base conditions
                return 0 
            sum1 = 0 
            if W >= wt[n-1] :
                sum1 = val[n-1] + helper(W - wt[n-1], n-1)
            sum2 = helper(W , n-1 )
            return max(sum1, sum2)
        return helper(W, len(wt))

    #  lru_cache T - O(n * w)    S - O(n * w)
    def knapSackRUnbound(self, wt: List, val: List, W: int) -> int:
        @lru_cache(None)
        def helper( W, n):
            if n == 0 or W <= 0:  # base conditions
                return 0   
            sum1 = 0 
            if W >= wt[n-1] :
                sum1 = val[n-1] + helper(W - wt[n-1], n)
            sum2 = helper(W , n-1 )
            return max(sum1, sum2)

        return helper(W, len(wt))

s = Solution()
wt = [1, 3, 4, 5]
val = [3, 4, 5, 7]
maxw = 7

# wt = [1, 1, 1]
# val = [10, 20, 30]
# maxw = 2

ans = s.knapSackR(wt, val, maxw)
print(ans)

ans1 = s.knapSackDP(wt, val, maxw)
print(ans1)

ans1 = s.knapSackRUnbound(wt, val, maxw)
print(ans1)