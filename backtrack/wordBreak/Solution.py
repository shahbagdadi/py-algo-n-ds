from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def helper(start, tmp):
            if start == N: 
                ans.append(tmp[:])
                return 
            for end in range(start+1, N+1):
                if s[start:end] in wordDict :
                    tmp.append(s[start:end])
                    helper(end,tmp)
                    tmp.pop()           
        ans , N = [], len(s)
        helper(0,[])
        return ans
s = Solution()
word = 'applepenapple'
wordList = ["apple", "pen"]
ans = s.wordBreak(word, wordList)
print(ans)