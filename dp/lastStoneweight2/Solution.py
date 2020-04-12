from typing import List

class Solution:
    def lastStoneWeightII(self, A: List[int]) -> int:
        '''
            To get the minimum the `right` 2 group of numbers should be formed such that after cancelling each other the remainder is minimum.
            ans = min({sum of group1} - {sum of group2})
            We do not know what the groups are so we try all possible combination by adding a number to all numbers so far (part of same group) 
            and substracting all numbers so far (cancellation with other group).
            the dp set below will have all the combinations and the minimum is the answer. We dont really need to know the groups that resulted in the answer
        '''
        dp = {0}
        for a in A:
            dp = {a + x for x in dp} | {a - x for x in dp}
            # print(dp)
        return min(abs(x) for x in dp)

s = Solution()
print(s.lastStoneWeightII([2,7,4,1,8,1]))

