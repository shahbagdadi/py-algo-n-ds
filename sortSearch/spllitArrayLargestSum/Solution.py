from typing import List
# Explanation - https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation
class Solution:

    def splitArray(self, nums: List[int], m: int) -> int:
        def feasable(threshold):
            cuts, curr_sum  = 1, 0
            for n in nums:
                curr_sum += n
                if curr_sum > threshold:
                    cuts, curr_sum = cuts+1, n
                    if cuts > m : return False
            return True
        
        l, r = max(nums), sum(nums) # search space is max number and sum of all numbers 
        while l < r:
            mid = (l + r)//2  # Threshold for a batch
            if feasable(mid): # can you make at-most m sub-arrays with maximum sum atmost mid (threshold)
                r = mid
            else:
                l = mid +1
        return l

s = Solution()
a = s.splitArray([7,2,5,10,8],2)
print(a)