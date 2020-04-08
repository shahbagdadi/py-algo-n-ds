from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        a = sorted(arr)
        i, j, L, ans = 0, 0, len(a), 0
        while j < L:
            if i == j or a[i] == a[j]:
                j += 1
            elif a[j] == a[i] + 1:
                ans += 1
                i += 1
            else:
                i += 1
        return ans


s = Solution()
print(s.countElements([1,1,2]))
