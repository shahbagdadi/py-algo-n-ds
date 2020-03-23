from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        i , stk , r = len(T)-1, [] , [0] * len(T)
        while i >= 0:
            while stk and T[i] >= stk[-1][0]:
                stk.pop()
            if stk : r[i] = stk[-1][1] - i
            stk.append((T[i],i))
            i -= 1
        return r

s = Solution()
a = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(a)