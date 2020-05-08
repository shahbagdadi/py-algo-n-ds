from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs : return 0
        dp = costs[0]
        for i in range(1,len(costs)):
            pre = dp[:]
            dp[0] = costs[i][0] + min(pre[1], pre[2])
            dp[1] = costs[i][1] + min(pre[0], pre[2])
            dp[2] = costs[i][2] + min(pre[0], pre[1])
        return min(dp)

s = Solution()
ip = [[17,2,17],[16,16,5],[14,3,19]]
ans = s.minCost(ip)
print(ans)