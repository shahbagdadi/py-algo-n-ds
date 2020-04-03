from typing import List
import bisect

class Solution:
    # T - O(n^2)   S - O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums : return 0
        dp = [0 for x in range(len(nums))]
        ans = 1
        for i in range(len(nums)):
            maxc = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxc = max(maxc, dp[j])
            dp[i] = maxc + 1
            ans = max(ans, dp[i])
        return ans

    
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            Patience sort - http://wordaligned.org/articles/patience-sort
            The cards which end up on top of the piles at the end of the sorting phase do form an increasing sequence, 
            this sequence may not be a subsequence of the original shuffled deck. We need to maintain back-pointers, implemented here as list indices
            T - O(n^2)   S - O(n)
        '''
        minend = [float('inf')] * (len(nums) + 1)
        for num in nums:
            minend[bisect.bisect_left(minend, num)] = num
            print(minend)
        return minend.index(float('inf'))


    def lengthOfLISBS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            print(tails)
            size = max(i + 1, size)
        return size

s = Solution()
print(s.lengthOfLIS([4, 10, 4, 3, 8, 1, 9]))
print(s.lengthOfLISBS([4, 10, 4, 3, 8, 1, 9]))
