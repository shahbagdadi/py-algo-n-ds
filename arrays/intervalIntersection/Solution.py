from typing import List
import sys


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j, LA, LB , res = 0, 0, len(A), len(B) , []
        while i < LA and j < LB:
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])

            if lo <= hi:
                res.append([lo, hi])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res


s = Solution()
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

# A = [[5,10]]
# B = [[3,10]]
ans = s.intervalIntersection(A, B)
print(ans)