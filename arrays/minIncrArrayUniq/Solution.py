from typing import List
import collections
import heapq

class Solution:
    #Union Find T - O(n) amortized    S - O(n)
    def minIncrementForUnique(self, A: List[int]) -> int:
        root = {}
        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]
        return sum(find(a) - a for a in A)

        

s = Solution()
ip = [3,2,1,2,1,7]
ans = s.minIncrementForUnique(ip)
print(ans)
        