from typing import List
import itertools
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum = ans = 0
        seen = Counter()
        seen[0] = 1
        for n in nums:
            csum += n
            ans += seen[csum-k]         # counter returns 0 if not found
            seen[csum] = seen[csum] + 1
        # print(seen)
        return ans


s = Solution()
a = s.subarraySum([1, -5, 3, 4, 2 , 0], 2)
print(a)
