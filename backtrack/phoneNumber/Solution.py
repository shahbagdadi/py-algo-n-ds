from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits : return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        def baktrack(idx, tmp) :
            if idx == len(digits) :
                ans.append(tmp)
                return
            for c in mapping[digits[idx]]:
                baktrack(idx+1,tmp+c)

        ans = []
        baktrack(0,'')
        return ans
        

s = Solution()
ip = "23"
ans = s.letterCombinations(ip)
print(ans)