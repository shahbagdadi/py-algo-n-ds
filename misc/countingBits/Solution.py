from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        while len(res) <= num:
            # res += [i+1 for i in res] # doing more work than needed so truncate as below
            res += [i+1 for i in res[:num+1 -len(res)]]
        return res
        

s = Solution()
ans = s.countBits(9)
print(ans)