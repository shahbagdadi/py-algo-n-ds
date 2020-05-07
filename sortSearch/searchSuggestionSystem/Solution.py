from bisect import bisect_left
from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        i , prefix , res = 0 , '' , []
        for c in searchWord:
            prefix += c
            i = bisect_left(products,prefix,i)
            res.append([x for x in products[i:i+3] if x.startswith(prefix) ])
        return res

s = Solution()
ip = ["bags","baggage","banner","box","cloths"]
word = 'bags'
ans = s.suggestedProducts(ip,word)
print(ans)