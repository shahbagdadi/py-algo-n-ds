from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for x in range(days[-1]+1)]
        travel_days = set(days)
        for d in range(days[-1]+1):
            if d not in travel_days:
                dp[d] = dp[d-1] 
            else :
                dp[d] = min(dp[max(0,d-1)]+ costs[0] , dp[max(0,d-7)]+ costs[1] , dp[max(0,d-30)]+ costs[2])
        print(dp)
        return dp[-1]

s = Solution()
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
ans = s.mincostTickets(days,costs)
print(ans)