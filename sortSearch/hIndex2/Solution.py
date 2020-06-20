from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if citations[mid] >= n-mid:
                r = mid - 1
            else:
                l = mid + 1
        return n-l

            

s = Solution()
ip = [0,1,3,5,6]
ans = s.hIndex(ip)
print(ans)