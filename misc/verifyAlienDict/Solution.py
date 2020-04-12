from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx = { c : i  for i, c in enumerate(order)}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1), len(w2))

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if order_idx[w1[j]] > order_idx[w2[j]] :
                        return False
                    break
            else: # only executed if for exited without break
                if len(w1) > len(w2) :
                    return False
        return True


s = Solution()
print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
