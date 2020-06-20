class Solution:
    # T - O(n^2)   S - O(n)
    def longestRepeatingSubstring(self, S: str) -> int:
        ans = 0
        for i in range(1, len(S)):
            if ans >= len(S)-i: 
                break 
                
            tmp = 0
            for x, y in zip(S[i:],S[:-i]):
                if x == y:
                    tmp += 1 
                    ans = max(ans, tmp)
                else:
                    tmp = 0 
        return ans

s = Solution()
ans = s.longestRepeatingSubstring('banana')
print(ans)