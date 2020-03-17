from typing import List

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l,h = 0, len(nums) -1 
        while l <= h :
            m = (l + h) // 2
            if nums[m] == t :
                return m
            if nums[l] <= nums[m] :
                if nums[l] <= t <= nums[m] :
                    h = m -1
                else :
                    l = m + 1
            else :
                if nums[m] <= t <= nums[h] :
                    l = m + 1
                else :
                    h = m - 1
        return -1

s = Solution()
a = s.search([4,5,6,7,0,1,2],3)
print(a)