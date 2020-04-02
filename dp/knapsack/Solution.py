from typing import List


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
    def knapSackR(self, wt: List, val: List, W: int) -> int:

        def helper(wt, val, W, n):
            if n == 0 or W == 0:  # base conditions
                return 0
            # If weight is higher than capacity then it is not included
            if (wt[n-1] > W):
                return helper(wt, val, W, n-1)
            # return either nth item being included or not
            else:
                return max(val[n-1] + helper(wt, val, W-wt[n-1], n-1), helper(wt, val, W, n-1))

        return helper(wt, val, W, len(wt))


s = Solution()
# wt = [1, 3, 4, 5]
# val = [1, 4, 5, 7]
# maxw = 7

wt = [1, 1, 1]
val = [10, 20, 30]
maxw = 2

ans = s.knapSackR(wt, val, maxw)
print(ans)

ans1 = s.knapSackDP(wt, val, maxw)
print(ans1)
