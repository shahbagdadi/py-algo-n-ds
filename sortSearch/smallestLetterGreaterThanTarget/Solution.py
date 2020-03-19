from typing import List
import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        pos = bisect.bisect(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]


s = Solution()
print(s.nextGreatestLetter(["c","f", "j"], "e"))
# r = [ ord(c) for c in ["c","f", "j"]]

# print(r)