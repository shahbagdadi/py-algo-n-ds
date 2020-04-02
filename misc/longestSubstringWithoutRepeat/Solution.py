class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        saw  = set()
        i = j = ans = 0
        while j < len(s):
            if s[j] in saw:
                saw.remove(s[i])
                i += 1
            else:
                saw.add(s[j])
                ans = max (ans,len(saw))
                j += 1
        return ans

s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))