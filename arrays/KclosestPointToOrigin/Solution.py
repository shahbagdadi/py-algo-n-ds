from typing import List
from math import sqrt
import heapq


class Solution:
    # T - O(n log n + K) for sorting
    def kClosest1(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda P: P[0] * P[0] + P[1] * P[1])
        return points[:K]

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            # python min heap so put the largest on top
            dist = -(x*x + y*y)
            if len(heap) == K:
                # push this element and pop the largest
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [[x, y] for _, x, y in heap]


s = Solution()
a = s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
print(a)
