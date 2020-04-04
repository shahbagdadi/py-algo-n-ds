from typing import List

class Solution:
    def mergeSort(self, a: List[int], b: int) -> List[int]:
        ans, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1
        ans += a[i:] + b[j:]
        return ans


s = Solution()
print(s.mergeSort([1, 2, 3], [2, 3, 6, 9, 14]))
