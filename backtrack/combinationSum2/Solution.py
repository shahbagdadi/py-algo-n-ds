from typing import List


class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking for powerset
        def backtrack(start, end, tmp, t):
            if t < 0:
                return
            elif t == 0:
                ans.append(tmp.copy())
            else:
                for i in range(start, end):
                    if i > start and nums[i] == nums[i-1]:
                        continue  # if dups in nums
                    tmp.append(nums[i])
                    backtrack(i+1, end, tmp, t-nums[i])
                    tmp.pop()
        ans = []
        # if dups in nums
        nums.sort()
        backtrack(0, len(nums), [], target)
        return ans


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
