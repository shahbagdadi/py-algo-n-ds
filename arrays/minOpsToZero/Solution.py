from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        l , w, mw = 0 , 0, -1
        for r in range(len(nums)) :
            w += nums[r]
            while w > total - x and l <= r :
                w -= nums[l]
                l += 1
            if w == total-x :
                mw = max(mw,r-l+1) 
        return len(nums)-mw if mw != -1 else -1
            
s = Solution()
ip = [1,1,4,2,3]
ans = s.minOperations(ip,5)
print(ans)