from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        pmax , cmax = 0 , 0 
        for n in nums:
            tmp = cmax
            cmax = max(pmax + n , cmax)
            pmax = tmp
        return cmax
        
s = Solution()
ip = [2,7,9,3,1]
ans = s.rob(ip)
print(ans)