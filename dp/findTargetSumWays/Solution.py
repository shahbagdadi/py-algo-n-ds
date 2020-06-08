from typing import List
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        N = len(nums)

        @lru_cache(None)
        def DP(idx,curSum):
            #Base case
            if idx == N and curSum == S :
                return 1
            if idx == N :
                return 0
            
            # Decisions
            positives = DP(idx+1, curSum + nums[idx])
            negatives = DP(idx+1, curSum - nums[idx])
            return positives + negatives
        return DP(0,0)

        
s = Solution()
ip = [1, 1, 1, 1, 1]
ans = s.findTargetSumWays(ip, 3)
print(ans)