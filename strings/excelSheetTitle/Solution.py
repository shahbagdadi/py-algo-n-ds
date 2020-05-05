from collections import Counter

class Solution:
    def convertToTitle(self, n: int) -> str:
        ans  = [] 
        while n > 0:
            r = (n-1) % 26
            ans.append(chr(r + ord('A')))
            n = (n-1) // 26
        return ''.join(ans[::-1])

s = Solution()
ans = s.convertToTitle(26)
print(ans)
