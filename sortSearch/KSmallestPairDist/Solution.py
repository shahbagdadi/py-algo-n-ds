class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        print(nums)
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            print(f'lo = {lo} , hi = {hi}, mi = {mi}')
            if possible(mi):
                print('possible')
                hi = mi
            else:
                print('not possible')
                lo = mi + 1
        return lo

s = Solution()
a = s.smallestDistancePair([1,1,8,5,4], 3)
print(f'result = {a}')