from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        cur_max , max_so_far, cur_min , min_so_far, total = 0 , -float('inf') , 0 , float('inf') , 0

        for x in A:
            cur_max = max(x, cur_max + x)
            max_so_far = max(max_so_far, cur_max)
            cur_min = min(x, cur_min + x)
            min_so_far = min(min_so_far, cur_min)
            total += x
        return max(max_so_far, total - min_so_far) if max_so_far > 0 else max_so_far


s = Solution()
ip = [1,-2,3,-2]
ans = s.maxSubarraySumCircular(ip)
print(ans)