from typing import List

# T - O(n * n)    S - O(1)


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()                                 # nlog(n)
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):                # n * n (for loop & while)
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target :                           # sum < target then go for larger number
                    l += 1
                elif s > target:                         # if Sum > target then go for smaller number
                    r -= 1
        return res

s = Solution()
ip = [-1, 2, 1, -4]
ans = s.threeSumClosest(ip,1)
print(ans)