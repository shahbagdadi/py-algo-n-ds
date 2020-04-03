from typing import List


class Solution:
    # T - 2-sum is O(Nlog N), 3-sum is O(N^2), 4-sum would be O(N^3)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def findNsum(l, r, target, N, result, results):
            # early termination
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target -
                                 nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        # N = 4 but can be used for any sum (try with 2, 3, 4, 5)
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
