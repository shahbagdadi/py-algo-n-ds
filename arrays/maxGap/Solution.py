from typing import List

class Solution:
    def maximumGap1(self, nums: List[int]) -> int:
        snums = sorted(nums)
        ans = 0
        for i in range(len(snums)-1):
            ans = max(ans,snums[i+1] - snums[i])
        return ans


    # Explanation - https://leetcode.com/problems/maximum-gap/solution/ bucket sort
    def maximumGap(self, num):
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        size = (b-a)//(len(num)-1) or 1
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in num:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))


s = Solution()
ans = s.maximumGap([3,6,9,1])
print(ans)