from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            if sum((i + m - 1) // m for i in nums) > threshold:
                l = m + 1
            else:
                r = m
        return l

s = Solution()
ip = [2,3,5,7,11]
ans = s.smallestDivisor(ip,11)
print(ans)