from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        N = len(matrix[0])
        height = [0] * (N +1)
        max_area = 0
        for row in matrix:
            for i in range(N):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            # print(height)   # histogram
            # calculate the max area of histogram
            stack = [-1]
            for i in range(N + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] -1
                    max_area = max(max_area, h * w)
                stack.append(i)
        return max_area

s = Solution()
ip = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
ans = s.maximalRectangle(ip)
print(ans)