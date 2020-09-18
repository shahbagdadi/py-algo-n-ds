from typing import List
from collections import Counter

class Solution :

    def largestComponentSize(self, a: List[int]) -> int:
        d = {}    # simple union find data structure
        def find(x):
            if x != d.setdefault(x,x):
                d[x] = find(d[x])
            return d[x]
        def union(x,y):
            d[find(x)]=find(y)

        for n in a:
            for i in range(2,int(n**0.5)+1): #just connect all the factors of the number  to the number
                if n%i: continue
                union(n,i)  
                union(n,n//i)

        counter = Counter(find(i) for i in a) 
        return max(counter.values())  # return the parent with maximum children

s = Solution()
ip = [2,3,6,7,4,12,21,39]
ans = s.largestComponentSize(ip)
print(ans)