from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)    # set the initial heights[-1] = 0
        ans , N = 0, len(heights)
        stack = [-1] # so we can consider 0 as height
        for i in range(N):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans

s = Solution()
# ans = s.largestRectangleArea([2,1,5,6,2,3])
ans = s.largestRectangleArea([1])
print(ans)