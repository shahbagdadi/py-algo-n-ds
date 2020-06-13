from typing import List
from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]

    
    def changeR(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        @lru_cache(None)
        def DP(i,amt):
            if amt == 0 : return 1
            if amt < 0 or i == N : return 0
            sum1 = DP(i,amt - coins[i])
            sum2 = DP(i+1, amt)
            return sum1 + sum2
        return DP(0,amount)

s = Solution()
ip = [1, 2, 5]
ans = s.change(5,ip)
print(ans)
ans2 = s.changeR(5,ip)
print(ans2)