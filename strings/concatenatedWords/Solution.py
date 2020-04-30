from typing import List
from functools import lru_cache


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        @lru_cache(None)
        def validWord(word):
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and suffix in word_set:
                        return True
                if prefix in word_set and validWord(suffix):
                    return True
                # if suffix in word_set and validWord(prefix):
                #     return True
            return False

        ans =[]
        word_set = set(words)
        for word in words:
            if validWord(word):
                ans.append(word)
        return ans



s = Solution()
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
ans = s.findAllConcatenatedWordsInADict(words)
print(ans)