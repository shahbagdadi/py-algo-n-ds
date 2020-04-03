
from typing import List

# T - O(n * n)    S - O(1)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()                                 # nlog(n)
        for i in range(len(nums)-2):                # n * n (for loop & while)
            if i > 0 and nums[i] == nums[i-1]:      # skip if num same as prev num
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:                           # sum < 0 then go for larger number
                    l += 1
                elif s > 0:                         # if Sum > 0 then go for smaller number
                    r -= 1
                else:
                    # if equal append to result
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:   # skip the dups on left
                        l += 1
                    while l < r and nums[r] == nums[r-1]:   # skip the dups on right
                        r -= 1
                    l += 1
                    r -= 1
        return res
