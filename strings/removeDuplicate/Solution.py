
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        rindex = { c : i for i,c in enumerate(s)}
        seen = set()
        stack = []
        for i,c in enumerate(s):
             if c not in seen:
                 while stack and c < stack[-1] and rindex[stack[-1]] > i :
                     x = stack.pop()
                     seen.remove(x)
                 stack.append(c)
                 seen.add(c)
        return ''.join(stack)

s = Solution()
ip = 'cbacdcbc'
ans = s.removeDuplicateLetters(ip)
print(ans)