from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            # if x less than first then return first k elements
            return arr[:k]
        if x >= arr[-1]:
            # if x greater than last then return last k elements
            return arr[-k:]
        l, h = 0, len(arr)-k                 # note h is kth element from last
        while l < h:                        # binary search to move the k element window
            m = (l+h) // 2
            # find wheather the left end or right end of window is closer in value to x
            if x-arr[m] > arr[m+k]-x:
                l = m + 1                   # slide window towards m+k
            else:
                h = m                       # slide window towards l
        return arr[l:l+k]


s = Solution()
print(s.findClosestElements([1, 2, 3, 4, 5], 4, 3))
