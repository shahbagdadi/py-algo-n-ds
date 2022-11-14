from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total , N = sum(nums), len(nums) 
        if N < k or total % k != 0 : return False
        bucket = [total//k] * k # k bucket with value total//k
        nums.sort(reverse=True)
        def backtrack(i) :
            if i == N : return True
            for j in range(k) :
                if bucket[j] >= nums[i] : 
                    bucket[j] -= nums[i]
                    if backtrack(i+1) : 
                        return True
                    bucket[j] += nums[i]
            return False
        
        return backtrack(0)

s = Solution()
ip = [4,3,2,3,5,2,1]
k = 4
ans = s.canPartitionKSubsets(ip,4)
print(ans)