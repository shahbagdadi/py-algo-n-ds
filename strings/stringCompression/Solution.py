from typing import List
import sys
class Solution:

    def compress(self, chars):
        anchor = j = 0
        for i, c in enumerate(chars):
            if i + 1 == len(chars) or chars[i + 1] != c:    # last char or this char is diff than next
                chars[j] = chars[anchor]                    # write the anchor char
                j += 1                                      # increment write pointer
                if i > anchor:                              # new anchor
                    for digit in str(i - anchor + 1):       # number of repeating char
                        chars[j] = digit                    # write the count
                        j += 1
                anchor = i + 1                              # point the anchor to the next different char
        print(chars)
        return j

s = Solution()
# ip = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
ip = ["a","a","b","b","c","c","c"]
ans = s.compress(ip)
print(ans)