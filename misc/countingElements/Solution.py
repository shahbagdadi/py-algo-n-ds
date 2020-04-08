from typing import List
from collections import Counter


class Solution:

    def countElements1(self, arr: List[int]) -> int:
        ''' T - O(nlogn) '''
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

    def countElements(self, arr: List[int]) -> int:
        ''' T - O(n) '''
        C = Counter(arr)
        return sum([C[x] for x in C if x+1 in C])


s = Solution()
print(s.countElements([1, 1, 2]))
