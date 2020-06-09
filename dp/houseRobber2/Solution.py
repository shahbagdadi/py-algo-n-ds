from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 : return nums[0]
        def helper(nums) :
            pmax , cmax = 0, 0
            for n in nums :
                tmp = cmax
                cmax = max(pmax + n , cmax)
                pmax = tmp
            return cmax
        return max(helper(nums[1:]), helper(nums[:-1]))

s = Solution()
ip = [1,2,3,1]
ans = s.rob(ip)
print(ans)