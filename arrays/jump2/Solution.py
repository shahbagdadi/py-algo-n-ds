from typing import List
import sys

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <=1: return 0
        l , r , jumps = 0, nums[0] , 1
        while r < len(nums)-1 :
            jumps += 1
            # you can land anywhere between l & r+1 in a jump and then use Num[i] to jump from there
            nxt = max( i + nums[i] for i in range(l, r+1)) 
            l , r = r, nxt
        return jumps

s = Solution()

ans = s.jump([3,2,1,0,4])
print(ans)