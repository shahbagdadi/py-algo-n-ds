from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = bisect.bisect_left(nums,target)
        hi = bisect.bisect(nums,target) - 1
        return [-1,-1] if target not in nums[lo:lo+1] else [lo,hi]

    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        def findFirst(n) :
            lo, hi = 0, len(nums)
            while lo < hi:
                m = (lo + hi) // 2
                if nums[m] >= n:
                    hi = m
                else:
                    lo = m + 1
            return lo
        lo = findFirst(target)
        return [lo, findFirst(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]       


s = Solution()
print(s.searchRange1([8,8,8,8,8,8,8,8],8))