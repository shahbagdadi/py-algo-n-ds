from typing import List
import collections
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList) # faster checks against a set
        res = []                    # result
        layer = {}                  # dict storing  word and how to get to it
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    return layer[w]         # if we reached end word we know how to get to it
                else:
                    for i in range(len(w)):                 # For each letter try all lettes a-z
                        for c in string.ascii_lowercase:
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:            # If the new word is in the word list. 
                                newlayer[neww]+=[j+[neww] for j in layer[w]]  # add new word to all sequences and form new layer element

            wordList -= set(newlayer.keys()) # remove visited words from dictionary to prevent loops
            layer = newlayer

        return res

wordList = ["hot","dot","dog","lot","log","cog"]
s = Solution()
ans = s.findLadders('hit', 'cog', wordList)
print(ans)