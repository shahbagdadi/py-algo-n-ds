from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = candidate = 0
        for n in nums:
            if not cnt:
                candidate = n
            if n == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate


s = Solution()
print(s.majorityElement([3, 2, 3]))
