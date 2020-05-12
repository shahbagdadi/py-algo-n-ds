from typing import List
import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:] + [0]):
            medians.append((window[k//2] + window[~(k//2)]) / 2.0)
            window.remove(a)
            bisect.insort(window, b)
        return medians

s = Solution()
ip = [1,3,-1,-3,5,3,6,7]
ans = s.medianSlidingWindow(ip,3)
print(ans)