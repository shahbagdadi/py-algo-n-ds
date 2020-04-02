from typing import List
import sys


class Solution:

    #  T - O( amount * coin)   S - O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for x in range(amount + 1)]
        for amt in range(1, len(dp)):
            min_coins = sys.maxsize
            for coin in coins:
                if amt - coin >= 0:
                    min_coins = min(min_coins, dp[amt-coin])
            dp[amt] = min_coins + 1 if min_coins != sys.maxsize else min_coins
            # print(dp)
        return -1 if dp[amount] == sys.maxsize else dp[amount]

    # T - O(amount ^ coin denominations)   S - O(coin denominations)
    def coinChangeR(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        min_coins = sys.maxsize
        for coin in coins:
            if amount - coin >= 0:
                min_coins = min(
                    min_coins, self.coinChangeR(coins, amount - coin))
        if min_coins != sys.maxsize:
            min_coins = min_coins + 1
        return min_coins


s = Solution()
print(s.coinChangeR([9, 6, 5, 1], 11))
print(s.coinChange([9, 6, 5, 1], 11))
