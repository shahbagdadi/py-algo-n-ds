from typing import List

class Solution:
    def searchRange(self, nums: List[int], K: int) -> List[int]:
        def findFirst(n) :
            lo, hi = 0, len(nums)
            while lo < hi:
                m = (lo + hi) // 2
                if nums[m] >= n:
                    hi = m
                else:
                    lo = m + 1
            return lo
        lo = findFirst(K)
        hi = findFirst(K+1)
        return hi - lo 

s = Solution()
ip = [1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,5,9]
ans = s.searchRange(ip,3)
print(ans)        