from typing import List
import sys
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = -sys.maxsize
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False

                
        

s = Solution()
ip = [8,4,7,5]
ans = s.find132pattern(ip)
print(ans)