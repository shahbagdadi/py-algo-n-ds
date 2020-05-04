from collections import Counter
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i, j, ans , L = 0, 0, 0, len(s)
        if L < 2 : return L
        ccnt = Counter()
        while j < L:
            c = s[j]
            if len(+ccnt) > 2 :
                ccnt[s[i]] -= 1
                i += 1
            if c in ccnt or len(+ccnt) < 3:
                ccnt[c] += 1
                j += 1
                if len(+ccnt) < 3 :
                    ans = max(ans , j - i )
            print(ccnt)   
        return ans

    def longSubstring(self, s):
        l , r = 0 , 0
        counts = defaultdict(int)
        # Slide the window down the string until we reach the end
        #
        # Loop invariant:
        # (1) The previously seen window is s[left:right]
        # (2) The right index - left index of window is always the length
        #     of the longest substring with <= 2 distinct characters
        while r < len(s):
            # Slide the right end up and update counts such that the window is now s[left:right+1]
            counts[s[r]] += 1
            r += 1
            # If the window has more than 2 characters, slide the left end of 
            # the window up and update counts such that the window is now s[left+1:right+1]
            if len(counts) > 2:
                counts[s[l]] -= 1
                if not counts[s[l]]:
                    del counts[s[l]]
                l += 1
        # The length of the window is the length of the longest valid substring
        return r - l
                


s = Solution()
ans = s.longSubstring('abacba')
print(ans)