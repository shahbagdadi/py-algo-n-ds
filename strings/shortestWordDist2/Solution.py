from typing import List
from collections import defaultdict


class WordDistance:

    def __init__(self, words: List[str]):
        self.location = defaultdict(list)
        for i,w in enumerate(words):
            self.location[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1 , l2 = self.location[word1], self.location[word2]
        p1 , p2 , ans = 0, 0 , float('inf')

        while p1 < len(l1) and p2 < len(l2):
            ans = min(ans , abs(l1[p1] - l2[p2]))
            if l1[p1] < l2[p2]:
                p1 += 1
            else: 
                p2 += 1
        return ans

        

ip = ["a", "a", "b", "c", "b"]
s = WordDistance(ip)
ans = s.shortest('a','b')
print(ans)